from aenum import Enum, IntEnum


class RespCode(IntEnum):
    Succeed = 0
    NotLogin = 100
    BusinessError = 101
    InvalidParams = 102
    NoBalance = 103
    MaxSending = 104
    NoProfit = 105
    NoPermission = 106
    NoBotOnline = 111
    AmountNotMatched = 112
    NoInventory = 201
    NoLotteryCount = 202
    WheelBlocked = 203
    NotOwnedGame = 204
    GameFull = 301
    InvalidGame = 302
    BadRequest = 400
    Maintenance = 401
    NotFound = 404
    Exception = 500


class KnowledgeType(IntEnum):
    AirPollution = 1 # '大气污染',
    FloraFauna = 2 # '动植物',
    SolidWaste = 3 # '固废',
    LightPollution = 4 # '光污染',
    EnvtInvention = 5 # '环保发明',
    EnvtEnergy = 6 # '环保能源',
    WaterResources = 7 # '水资源',
    Soil = 8 # '土壤',
    Noise = 9 # '噪声'