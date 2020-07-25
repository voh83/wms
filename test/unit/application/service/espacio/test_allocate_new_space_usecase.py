import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\wms")
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.infrastructure.domain.espacio.in_memory.in_memory_espacio_repository import InMemoryEspacioRepository
from src.app.application.service.espacio.new_space_usecase import NewSpaceUseCase
from src.app.application.service.espacio.allocate_espacio_request import AllocateEspacioRequest
from src.app.domain.model.shared.exceptions import NonExistingWarehouseException, SpaceAlreadyExistException
from src.app.domain.model.bodega.bodega import Bodega
import pytest


def test_allocate_new_space():
    bodega_repo = InMemoryBodegaRepository()
    espacio_repo = InMemoryEspacioRepository()
    bodega = Bodega('Bodega-123456')
    wh_id= bodega.get_id()
    space_name = 'space-1'
    space_maximum_volume = 10
    space_maximum_weight = 100  
    bodega_repo.append(bodega)
    NewSpaceUseCase(bodega_repo,espacio_repo).execute(AllocateEspacioRequest(wh_id, space_name, space_maximum_volume, space_maximum_weight))
    assert False #FIXME: Assert the real things
    
def test_allocate_new_space_in_empty_warehouse_throws_NonExistingWarehouseException():
    bodega_repo = InMemoryBodegaRepository()
    espacio_repo = InMemoryEspacioRepository()
    wh_name = 'Bodega-123456'
    space_name = 'space-1'
    space_maximum_volume = 10
    space_maximum_weight = 100  
    with pytest.raises(NonExistingWarehouseException, match=wh_name):
        NewSpaceUseCase(bodega_repo,espacio_repo).execute(AllocateEspacioRequest(wh_name, space_name, space_maximum_volume, space_maximum_weight))
    