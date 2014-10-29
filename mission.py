# -*- coding: utf-8 -*-

import pawn

MISSION_OBJECTIVE_TYPE_BEAT_ALL = 0
MISSION_OBJECTIVE_TYPE_BEAT_TARGET = 1
MISSION_OBJECTIVE_TYPE_RETREAT = 2
MISSION_OBJECTIVE_TYPE_HOLD = 3


class Mission:
    def __init__(self, mission_id, mission_title='', mission_introduction='', objective_type=0, turn_limit=-1):
        self.mission_id = mission_id
        self.mission_title = mission_title
        self.mission_introduction = mission_introduction
        self.objective_type = objective_type
        self.player_roster = []
        self.enemy_roster = []
        self.friend_roster = []
        self.turn_limit = turn_limit


    def set_objective_targets(self, targets):
        self.beat_targets = targets

    def set_player_roster(self, roster):
        self.player_roster = roster

    def set_enemy_roster(self, roster):
        self.enemy_roster = roster

    def set_friend_roster(self, roster):
        self.friend_roster = roster


test_mission = Mission(1, u'卫温求夷洲'
    , u'吴国将军卫温与诸葛直在台湾南端登陆，收伏岛上部落后，因水土不服、疾病滋生等原因，士兵死亡率将近八九成，最终俘虏当地数千人离开。回国后因任务完成不力，二人被孙权所杀。'
    , MISSION_OBJECTIVE_TYPE_BEAT_ALL, 20)

test_mission.set_player_roster(
    [
        (260, (3, 3) , pawn.DIRECTION_DOWN, pawn.ARM_MELEE, pawn.MOBILE_WALK , 0 , True , False),
        (261, (3, 4) , pawn.DIRECTION_DOWN, pawn.ARM_MELEE, pawn.MOBILE_MOUNT , 0 , True , False)
    ]
)


test_mission.set_enemy_roster(
    [
        (262, (8, 3) , pawn.DIRECTION_UP, pawn.ARM_MELEE, pawn.MOBILE_WALK , 1 , False , True),
        (263, (8, 4) , pawn.DIRECTION_UP, pawn.ARM_MELEE, pawn.MOBILE_WALK , 1 , False , True)
    ]
)


test_mission.set_friend_roster(
    [
        (280, (2, 3) , pawn.DIRECTION_DOWN, pawn.ARM_MELEE, pawn.MOBILE_WALK , 0 , False , True),
        (280, (2, 4) , pawn.DIRECTION_DOWN, pawn.ARM_MELEE, pawn.MOBILE_WALK , 0 , False , True)
    ]
)