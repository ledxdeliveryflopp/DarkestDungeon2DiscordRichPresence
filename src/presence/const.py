

class StateConst:
    """Состояния игры"""
    states: dict = {"LOADING": {"ru": "Загрузка", "en": "Loading"},
                    "MAIN_MENU": {"ru": "В главном меню", "en": "In main menu"},
                    "DRIVING":  {"ru": "Путешествует по", "en": "travels across the"},
                    "COMBAT": {"ru": "В бою с", "en": "In battle against"},
                    "RESULTS": {"ru": "Просматривает результаты боя", "en": "Views the results of the battle"},
                    "INN": {"ru": "В трактире", "en": "in the inn"},
                    "EMBARK": {"ru": "начинает путешествие", "en": "Embark"},
                    "HERO_SELECT": {"ru": "Выбирает героев", "en": "Chooses heroes"}}


class ProposalConst:
    """Текст при отсутствии локации и врага"""
    proposal: dict = {"COMBAT": {"ru": "неизвестным врагом", "en": "an unknown enemy"},
                      "DRIVING": {"ru": "неизвестной локации", "en": "unknown location"}}


class EnemyConst:
    """Названия врагов(группы врагов по техническому названию) и их код"""
    enemy: dict = {"fanatic_flayer": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_flayer_b": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_flayer_ignited": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_flayer_corpse": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_immolatist_b": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_immolatist": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_pit_fighter": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_whipper_corpse": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_whipper": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_whipper_b": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},
                   "fanatic_whipper_ignited": {"ru": "Изуверами", "en": "Fanatics", "enemy_code": "fanatic"},

                   "cultist_altar": {"ru": "Культистами", "en": "Cultists", "enemy_code": "cultist"},
                   "cultist_herald": {"ru": "Культистами", "en": "Cultists", "enemy_code": "cultist"},
                   "cultist_evangelist": {"ru": "Культистами", "en": "Cultists", "enemy_code": "cultist"},
                   "cultist_cherub": {"ru": "Культистами", "en": "Cultists", "enemy_code": "cultist"},

                   "shared_barricade_swordsman": {"ru": "Солдатами", "en": "Military", "enemy_code": "military"},
                   "shared_barricade_spearman": {"ru": "Солдатами", "en": "Military", "enemy_code": "military"},

                   "plague_eater_livestock": {"ru": "Несытями", "en": "Plague eaters", "enemy_code": "plague"},
                   "plague_eater_livestock_b": {"ru": "Несытями", "en": "Plague eaters", "enemy_code": "plague"},
                   "plague_eater_maid": {"ru": "Несытями", "en": "Plague eaters", "enemy_code": "plague"},
                   "plague_eater_maid_b": {"ru": "Несытями", "en": "Plague eaters", "enemy_code": "plague"},
                   "plague_eater_butcher_b": {"ru": "Несытями", "en": "Plague eaters", "enemy_code": "plague"},
                   "plague_eater_butcher": {"ru": "Несытями", "en": "Plague eaters", "enemy_code": "plague"},
                   "plague_eater_dinner_cart": {"ru": "Несытями", "en": "Plague eaters", "enemy_code": "plague"},

                   "shared_pillager_melee": {"ru": "Бандитами", "en": "Pillagers", "enemy_code": "pillager"},
                   "shared_pillager_firemouth": {"ru": "Бандитами", "en": "Pillagers", "enemy_code": "pillager"},
                   "shared_pillager_mongrel": {"ru": "Бандитами", "en": "Pillagers", "enemy_code": "pillager"},
                   "shared_pillager_ranged": {"ru": "Бандитами", "en": "Pillagers", "enemy_code": "pillager"},

                   "beastmen_tribewalker": {"ru": "Зверолюдьми", "en": "Beastmens", "enemy_code": "beastmen"},
                   "beastmen_huntsman": {"ru": "Зверолюдьми", "en": "Beastmens", "enemy_code": "beastmen"},
                   "beastmen_rot_claw": {"ru": "Зверолюдьми", "en": "Beastmens", "enemy_code": "beastmen"},
                   "beastmen_tribecaller": {"ru": "Зверолюдьми", "en": "Beastmens", "enemy_code": "beastmen"},
                   "beastmen_rot_claw_elite": {"ru": "Зверолюдьми", "en": "Beastmens", "enemy_code": "beastmen"},

                   "shared_lost_soul_yeoman": {"ru": "Дохляками", "en": "Gaunts", "enemy_code": "gaunt"},
                   "shared_ghoul": {"ru": "Дохляками", "en": "Gaunts", "enemy_code": "gaunt"},
                   "shared_lost_soul": {"ru": "Дохляками", "en": "Gaunts", "enemy_code": "gaunt"},
                   "shared_lost_soul_widow": {"ru": "Дохляками", "en": "Gaunts", "enemy_code": "gaunt"},
                   "shared_lost_soul_urchin": {"ru": "Дохляками", "en": "Gaunts", "enemy_code": "gaunt"},  # шкилет

                   "coastal_bosun": {"ru": "Рыболюдьми", "en": "Fisherfolks", "enemy_code": "fisherfolk"},
                   "coastal_fish_monger": {"ru": "Рыболюдьми", "en": "Fisherfolks", "enemy_code": "fisherfolk"},
                   "coastal_captain": {"ru": "Рыболюдьми", "en": "Fisherfolks", "enemy_code": "fisherfolk"},
                   "coastal_cabin_boy": {"ru": "Рыболюдьми", "en": "Fisherfolks", "enemy_code": "fisherfolk"},

                   "shared_carrion_eater": {"ru": "Тварями", "en": "Creatures", "enemy_code": "creatures"},
                   "shared_carrion_eater_mutated": {"ru": "Тварями", "en": "Creatures", "enemy_code": "creatures"},
                   "shared_carrion_eater_corpse": {"ru": "Тварями", "en": "Creatures", "enemy_code": "creatures"},
                   "shared_dog_rabid": {"ru": "Тварями", "en": "Creatures", "enemy_code": "creatures"},
                   "shared_spider_webber": {"ru": "Тварями", "en": "Creatures", "enemy_code": "creatures"},
                   "shared_spider_spitter": {"ru": "Тварями", "en": "Creatures", "enemy_code": "creatures"},

                   "lost_battalion_foot_soldier": {"ru": "Кадаврами", "en": "Cadavers", "enemy_code": "cadaver"},
                   "lost_battalion_knight": {"ru": "Кадаврами", "en": "Cadavers", "enemy_code": "cadaver"},
                   "lost_battalion_knight_b": {"ru": "Кадаврами", "en": "Cadavers", "enemy_code": "cadaver"},
                   "lost_battalion_bishop": {"ru": "Кадаврами", "en": "Cadavers", "enemy_code": "cadaver"},
                   "lost_battalion_drummer": {"ru": "Кадаврами", "en": "Cadavers", "enemy_code": "cadaver"},
                   "lost_battalion_arbalist": {"ru": "Кадаврами", "en": "Cadavers", "enemy_code": "cadaver"},
                   "lost_battalion_arbalist_b": {"ru": "Кадаврами", "en": "Cadavers", "enemy_code": "cadaver"}}


class ImagesConst:
    """Изображения для discord"""
    game_mode_images: dict = {"main": "big_logo", "kingdoms": "kingdoms"}


class LocationConst:
    """Названия локаций и их код"""
    locations_embark: dict = {"embark_camp_tundra": {"ru": "Тундре", "en": "Tundra", "location_code": "tundra"},
                              "embark_kingdom_tundra": {"ru": "Тундре", "en": "Tundra", "location_code": "tundra"},

                              "embark_kingdom_farm": {"ru": "Смрадью", "en": "Foetor", "location_code": "farm"},
                              "embark_camp_farm": {"ru": "Смрадью", "en": "Foetor", "location_code": "farm"},

                              "embark_kingdom_coast": {"ru": "Морготью", "en": "Shroud", "location_code": "coast"},
                              "embark_camp_coast": {"ru": "Морготью", "en": "Shroud", "location_code": "coast"},

                              "embark_camp_forest": {"ru": "Чернолесью", "en": "Tangle", "location_code": "forest"},
                              "embark_kingdom_forest": {"ru": "Чернолесью", "en": "Tangle", "location_code": "forest"},

                              "embark_kingdom_city": {"ru": "Поградью", "en": "Sprawl", "location_code": "city"},
                              "embark_camp_city": {"ru": "Поградью", "en": "Sprawl", "location_code": "city"}}

    locations_fog: dict = {"driving_tundra_environment_lighting": {"ru": "Тундре", "en": "Tundra",
                                                                   "location_code": "tundra"},

                           "driving_farm_environment_lighting": {"ru": "Смрадью", "en": "Foetor",
                                                                 "location_code": "farm"},

                           "driving_coast_environment_lighting": {"ru": "Морготью", "en": "Shroud",
                                                                  "location_code": "coast"},

                           "driving_forest_environment_lighting": {"ru": "Чернолесью", "en": "Tangle",
                                                                   "location_code": "forest"},

                           "driving_city_environment_lighting": {"ru": "Поградью", "en": "Sprawl",
                                                                 "location_code": "city"},

                           "driving_valley_environment_lighting": {"ru": "Долине", "en": "Valley",
                                                                   "location_code": "valley"}}
