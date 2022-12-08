from enum import Enum
from ks_constants.devs import Developer
from ks_constants.locale import Language


class Map(Enum):
    Classic = (0,
               {Language.English: 'Classic', Language.Korean: '기본'},
               "CLASSIC",
               Developer.Luminous,
               ["Base.SC2Data/GameData/Terrain/Classic.xml"],
               "maps/classic.SC2Map",
               False,
               None)
    Duck_Map = (1,
                {Language.English: 'Duck Map', Language.Korean: '오리'},
                "DUCK_MAP",
                Developer.Duck,
                ["Base.SC2Data/GameData/Terrain/DuckMap.xml"],
                "maps/duck_map.SC2Map",
                True,
                None)
    Four_Seasons = (4,
                    {Language.English: 'Four Seasons', Language.Korean: '사계절'},
                    "ZERUS_VOLCANOES",
                    Developer.Luminous,
                    ["Base.SC2Data/GameData/Terrain/FourSeasons.xml"],
                    "maps/four_seasons.SC2Map",
                    True,
                    None)
    Zerus_Volcanoes = (2,
                       {Language.English: 'Zerus Volcanoes', Language.Korean: '제루스 화산'},
                       "FOUR_SEASONS",
                       Developer.Luminous,
                       ["Base.SC2Data/GameData/Terrain/ZerusVolcanoes.xml"],
                       "maps/zerus_volcanoes.SC2Map",
                       True,
                       None)
    Ruins_Of_Imladoon = (3,
                         {Language.English: 'Ruins of Imladoon', Language.Korean: '임라둔의 잔해'},
                         "RUINS_OF_IMLADOON",
                         Developer.Fatline,
                         ["Base.SC2Data/GameData/Terrain/RuinsOfImladoon.xml"],
                         "maps/ruins_of_imladoon.SC2Map",
                         True,
                         Developer.Templar)
    Heart_Of_Amethyst = (5,
                         {Language.English: 'Heart of Amethyst', Language.Korean: '자수정의 심장'},
                         "HEART_OF_AMETHYST",
                         Developer.Luminous,
                         ["Base.SC2Data/GameData/Terrain/HeartOfAmethyst.xml"],
                         "maps/heart_of_amethyst.SC2Map",
                         False,
                         None)
    Vintage_Shores = (6,
                      {Language.English: 'Vintage Shores', Language.Korean: '빈티지 해변'},
                      "VINTAGE_SHORES",
                      Developer.Templar,
                      ["Base.SC2Data/GameData/Terrain/VintageShores.xml"],
                      "maps/vintage_shores.SC2Map",
                      False,
                      None)
    Aiur_Fountains = (7,
                      {Language.English: 'Aiur Fountains', Language.Korean: '아이어 분수'},
                      "AIUR_FOUNTAINS",
                      Developer.Luminous,
                      ["Base.SC2Data/GameData/Terrain/AiurFountains.xml"],
                      "maps/aiur_fountains.SC2Map",
                      False,
                      None)
    Kaldir_Cliffs = (8,
                     {Language.English: 'Kaldir Cliffs', Language.Korean: '칼디르 절벽'},
                     "KALDIR_CLIFFS",
                     Developer.Understudy,
                     ["Base.SC2Data/GameData/Terrain/KaldirCliffs.xml"],
                     "maps/kaldir_cliffs.SC2Map",
                     True,
                     None)
    Lost_Tides = (9,
                     {Language.English: 'Lost Tides', Language.Korean: '사라진 물의 흐름'},
                     "LOST_TIDES",
                     Developer.Templar,
                     ["Base.SC2Data/GameData/Terrain/LostTides.xml"],
                     "maps/lost_tides.SC2Map",
                     False,
                     None)    

    # galaxy representation is the string value of the Preset in KS2 Galaxy
    def __init__(self,
                 index: int,
                 name_dict: dict,
                 galaxy_representation: str,
                 original_author: Developer,
                 custom_file_list: list[str],
                 file_path: str,
                 is_active: bool = False,
                 current_author: Developer = None):
        self._index = index
        self._name_dict = name_dict
        self._galaxy_representation = galaxy_representation
        self._custom_file_list = custom_file_list
        self._file_path = file_path
        self._original_author = original_author
        self._current_author = original_author if current_author is None else current_author
        self._is_active = is_active

    @classmethod
    def from_index(cls, index):
        return _maps_list[index]

    def get_index(self):
        return self._index

    def get_name(self, locale: Language):
        return self._name_dict[locale]

    def get_english_name(self):
        return self.get_name(Language.English)

    def get_galaxy_representation(self):
        return self._galaxy_representation

    def original_author(self):
        return self._original_author

    def current_author(self):
        return self._current_author

    def file_path(self):
        return self._file_path

    def is_active(self):
        return self._is_active

    def custom_file_list(self):
        return self._custom_file_list


_maps_list = list(Map)
