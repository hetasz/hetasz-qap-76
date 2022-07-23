from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(fillter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, fillter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбус', animal_type='двортерьер',
                                     age='2', pet_photo='images/cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Супербарбус", "двортерьер", "2", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Супермурзик', animal_type='Котэ', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


"""Десять новых тестов"""


def test_successful_add_new_pet_without_photo(name='Брабусик', animal_type='терьер', age='4'):
    """Удачное добавление питомца без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_successful_add_pet_photo(name='Брабусик', animal_type='терьер',
                                  age='4', pet_photo='images/cat1.jpg'):
    """Удачная установка фото для питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = None
    for x in my_pets['pets']:
        if x['name'] == name and x['pet_photo'] == '':
            pet_id = x['id']
            break
    if (len(my_pets['pets']) == 0) or (pet_id is None):
        _, new_pet = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
        pet_id = new_pet["id"]

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo'] != ''


def test_get_api_key_for_invalid_user(email='invalid@email.com', password='invalid_password'):
    """Попытка авторизации неверными учетными данными"""
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_all_pets_with_invalid_key(fillter='my_pets'):
    """Передача неверного ключа авторизации"""
    auth_key = {'key': '0'}
    status, result = pf.get_list_of_pets(auth_key, fillter)
    assert status == 403


def test_bad_type_picture(name='Брабусик', animal_type='ласка',
                          age='4', pet_photo='images/pinemartenrock.gif'):
    """Загрузка картинки неверного типа"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, new_pet = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    pet_id = new_pet["id"]

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
    assert status == 400  # 500


def test_set_picture_without_authorization(pet_photo='images/cat1.jpg'):
    """Загрузка картинки чужому питомцу"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    for x in my_pets['pets']:
        pet_id = x['id']
        status, _ = pf.delete_pet(auth_key, pet_id)

    _, result = pf.get_list_of_pets(auth_key, '')
    pet_id = result['pets'][0]['id']

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
    assert status == 500  # 403


def test_del_pet_without_authorization():
    """Удаление чужого питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    for x in my_pets['pets']:
        pet_id = x['id']
        status, _ = pf.delete_pet(auth_key, pet_id)

    _, result = pf.get_list_of_pets(auth_key, '')
    if len(result['pets']) > 0:
        pet_id = result['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)
        assert status == 200  # 403
    else:
        raise Exception("There is no pets")


def test_add_new_pet_with_empty_data(name='', animal_type='',
                                     age='', pet_photo='images/cat1.jpg'):
    """Создание питомца с пустыми данными"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_with_invalid_data(name='"; DROP TABLE pets;',
                                       animal_type='<a href="ya.ru">google.com</a>',
                                       age='пять', pet_photo='images/cat1.jpg'):
    """Создание питомца с недопустимыми данными"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_pet_with_invalid_data(name='"<script>alert("Hello, world!")</script>',
                                      animal_type='<script>document.getElementByID("body").disabled=true</script>',
                                      age='\' or \'a\' = \'a\'; DROP TABLE users;'):
    """Обновление питомца недопустимыми данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == age
    else:
        raise Exception("There is no my pets")
