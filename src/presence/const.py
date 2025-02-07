
class StateConst:
    """Состояния игры"""
    states: dict = {"LOADING": "Загрузка", "MAIN_MENU": "В главном меню", "DRIVING": "Путешествует по",
                    "COMBAT": "В бою", "RESULTS": "Просматривает результаты боя", "INN": "В трактире",
                    "EMBARK": "начинает путешествие"}


class EnemyConst:
    """Названия врагов(группы врагов по техническому названию) и их код"""
    enemy: dict = {"fanatic_flayer": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_flayer_b": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_flayer_ignited": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_flayer_corpse": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_immolatist_b": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_immolatist": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_pit_fighter": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_whipper_corpse": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_whipper": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_whipper_b": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},
                   "fanatic_whipper_ignited": {"enemy_name": "Изуверами", "enemy_code": "fanatic"},

                   "cultist_altar": {"enemy_name": "Культистами", "enemy_code": "cultist"},
                   "cultist_herald": {"enemy_name": "Культистами", "enemy_code": "cultist"},
                   "cultist_evangelist": {"enemy_name": "Культистами", "enemy_code": "cultist"},
                   "cultist_cherub": {"enemy_name": "Культистами", "enemy_code": "cultist"},

                   "shared_barricade_swordsman": {"enemy_name": "Солдатами", "enemy_code": "military"},
                   "shared_barricade_spearman": {"enemy_name": "Солдатами", "enemy_code": "military"},

                   "plague_eater_livestock": {"enemy_name": "Несытями", "enemy_code": "plague"},
                   "plague_eater_livestock_b": {"enemy_name": "Несытями", "enemy_code": "plague"},
                   "plague_eater_maid": {"enemy_name": "Несытями", "enemy_code": "plague"},
                   "plague_eater_maid_b": {"enemy_name": "Несытями", "enemy_code": "plague"},
                   "plague_eater_butcher_b": {"enemy_name": "Несытями", "enemy_code": "plague"},
                   "plague_eater_butcher": {"enemy_name": "Несытями", "enemy_code": "plague"},
                   "plague_eater_dinner_cart": {"enemy_name": "Несытями", "enemy_code": "plague"},

                   "shared_pillager_melee": {"enemy_name": "Бандитами", "enemy_code": "pillager"},
                   "shared_pillager_firemouth": {"enemy_name": "Бандитами", "enemy_code": "pillager"},
                   "shared_pillager_mongrel": {"enemy_name": "Бандитами", "enemy_code": "pillager"},

                   "beastmen_tribewalker": {"enemy_name": "Зверолюдьми", "enemy_code": "beastmen"},
                   "beastmen_huntsman": {"enemy_name": "Зверолюдьми", "enemy_code": "beastmen"},
                   "beastmen_rot_claw": {"enemy_name": "Зверолюдьми", "enemy_code": "beastmen"},
                   "beastmen_tribecaller": {"enemy_name": "Зверолюдьми", "enemy_code": "beastmen"},

                   "shared_lost_soul_yeoman": {"enemy_name": "Дохляками", "enemy_code": "gaunt"},
                   "shared_ghoul": {"enemy_name": "Дохляками", "enemy_code": "gaunt"},
                   "shared_lost_soul": {"enemy_name": "Дохляками", "enemy_code": "gaunt"},
                   "shared_lost_soul_widow": {"enemy_name": "Дохляками", "enemy_code": "gaunt"},
                   "shared_lost_soul_urchin": {"enemy_name": "Дохляками", "enemy_code": "gaunt"},  # шкилет

                   "coastal_bosun": {"enemy_name": "Рыболюдьми", "enemy_code": "fisherfolk"},
                   "coastal_fish_monger": {"enemy_name": "Рыболюдьми", "enemy_code": "fisherfolk"},
                   "coastal_captain": {"enemy_name": "Рыболюдьми", "enemy_code": "fisherfolk"},
                   "coastal_cabin_boy": {"enemy_name": "Рыболюдьми", "enemy_code": "fisherfolk"},

                   "shared_carrion_eater": {"enemy_name": "Тварями", "enemy_code": "creatures"},
                   "shared_carrion_eater_mutated": {"enemy_name": "Тварями", "enemy_code": "creatures"},
                   "shared_carrion_eater_corpse": {"enemy_name": "Тварями", "enemy_code": "creatures"},
                   "shared_dog_rabid": {"enemy_name": "Тварями", "enemy_code": "creatures"},
                   "shared_spider_webber": {"enemy_name": "Тварями", "enemy_code": "creatures"},
                   "shared_spider_spitter": {"enemy_name": "Тварями", "enemy_code": "creatures"},

                   "lost_battalion_foot_soldier": {"enemy_name": "Кадаврами", "enemy_code": "cadaver"},
                   "lost_battalion_knight": {"enemy_name": "Кадаврами", "enemy_code": "cadaver"},
                   "lost_battalion_knight_b": {"enemy_name": "Кадаврами", "enemy_code": "cadaver"},
                   "lost_battalion_bishop": {"enemy_name": "Кадаврами", "enemy_code": "cadaver"},
                   "lost_battalion_drummer": {"enemy_name": "Кадаврами", "enemy_code": "cadaver"},
                   "lost_battalion_arbalist": {"enemy_name": "Кадаврами", "enemy_code": "cadaver"},
                   "lost_battalion_arbalist_b": {"enemy_name": "Кадаврами", "enemy_code": "cadaver"}}


class ImagesConst:
    """Изображения для discord"""
    game_mode_images: dict = {"main": "big_logo", "kingdoms": "kingdoms"}


class LocationConst:
    """Названия локаций и их код"""
    locations_embark: dict = {"embark_camp_tundra": {"location_name": "Тундре", "location_code": "tundra"},
                              "embark_kingdom_tundra": {"location_name": "Тундре", "location_code": "tundra"},

                              "embark_kingdom_farm": {"location_name": "Смрадью", "location_code": "farm"},
                              "embark_camp_farm": {"location_name": "Смрадью", "location_code": "farm"},

                              "embark_kingdom_coast": {"location_name": "Морготью", "location_code": "coast"},
                              "embark_camp_coast": {"location_name": "Морготью", "location_code": "coast"},

                              "embark_camp_forest": {"location_name": "Чернолесью", "location_code": "forest"},
                              "embark_kingdom_forest": {"location_name": "Чернолесью", "location_code": "forest"},

                              "embark_kingdom_city": {"location_name": "Поградью", "location_code": "city"},
                              "embark_camp_city": {"location_name": "Поградью", "location_code": "city"}}

    locations_fog: dict = {"driving_tundra_environment_lighting": {"location_name": "Тундре",
                                                                   "location_code": "tundra"},
                           "driving_farm_environment_lighting": {"location_name": "Смрадью",
                                                                 "location_code": "farm"},
                           "driving_coast_environment_lighting": {"location_name": "Морготью",
                                                                  "location_code": "coast"},
                           "driving_forest_environment_lighting": {"location_name": "Чернолесью",
                                                                   "location_code": "forest"},
                           "driving_city_environment_lighting": {"location_name": "Поградью",
                                                                 "location_code": "city"}}
