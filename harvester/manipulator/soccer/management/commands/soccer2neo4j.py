# coding: utf-8
from django.core.management.base import BaseCommand
from soccer import models
from utils.neo4j_driver import get_driver
from utils.queryset_iterator import queryset_iterator


class Command(BaseCommand):
    def _start_session(self):
        driver = get_driver()
        self.session = driver.session()

    def add_competition(self, tx, obj):
        comp_data = []
        if obj.short_name:
            comp_data.append(" short_name:'%s'" % obj.short_name)
        if obj.en_name:
            comp_data.append(" en_name:'%s'" % obj.en_name)
        tx.run("MERGE (nation:Nation{name:'%s'}) MERGE (comp:Competition{name:'%s'}) " % (obj.nation, obj.name) +
               "SET comp+= {" + ",".join(comp_data) + "} MERGE (comp) -[:BELONG_TO]-> "
               "(nation)")

    def add_club(self, tx, obj):
        club_data = []
        if obj.short_name:
            club_data.append(" short_name:'%s'" % obj.short_name)
        if obj.en_name:
            club_data.append(" en_name:'%s'" % obj.en_name)
        cypher = "MERGE (nation:Nation{name:'%s'}) " % obj.nation + \
                 "MERGE (club:Club{name:'%s'}) " % obj.name + \
                 (("SET club+= {" + ",".join(club_data) + "}") if club_data else "") + \
                 " MERGE (club) -[:LOCATE_IN]-> (nation) " + \
                 " ".join(["MERGE (comp:Competition{name:'%s'}) MERGE (club) -[:JOIN_IN]-> (comp)" % c.name
                           for c in obj.competitions.all()])
        print(cypher)
        tx.run(cypher)

    def add_nation_team(self, tx, obj):
        nt_data = []
        if obj.short_name:
            nt_data.append(" short_name:'%s'" % obj.short_name)
        if obj.en_name:
            nt_data.append(" en_name:'%s'" % obj.en_name)
        cypher = "MERGE (nation:Nation{name:'%s'}) " % obj.nation + \
                 "MERGE (nt:NationTeam{name:'%s'}) " % obj.name + \
                 (("SET club+= {" + ",".join(nt_data) + "}") if nt_data else "") + \
                 "MERGE (nt) -[:TEAM_OF]-> (nation) " + \
                 " ".join(["MERGE (comp:Competition{name:'%s'}) MERGE (nt) -[:JOIN_IN]-> (comp)" % c.name
                           for c in obj.competitions.all()])
        print(cypher)
        tx.run(cypher)

    def add_player(self, tx, obj):
        player_data = []
        if obj.name:
            player_data.append("name:'%s'" % str(obj.name))
        if obj.alias:
            player_data.append("alias:%s" % str(obj.alias))
        if obj.en_name:
            player_data.append(" en_name:'%s'" % obj.en_name)
        if obj.nick_name:
            player_data.append(" nick_name:%s" % obj.nick_name)
        if obj.gender:
            player_data.append(" gender:'%s'" % obj.get_gender_display())
        if obj.height:
            player_data.append(" height:%d" % obj.height)
        if obj.birth:
            player_data.append(" birth:'%s'" % obj.birth.strftime('%Y-%m-%d'))
        if obj.age:
            player_data.append(" age:%d" % obj.age)
        if obj.foot:
            player_data.append(" foot:'%s'" % obj.foot)
        if obj.field:
            player_data.append(" field:'%s'" % obj.field)
        if obj.positions:
            player_data.append(" positions:%s" % obj.positions)
        if obj.number:
            player_data.append(" number:%d" % obj.number)
        if obj.price:
            player_data.append(" price:%d" % obj.price)
        if obj.joined:
            player_data.append(" joined:'%s'" % obj.joined.strftime('%Y-%m-%d'))
        if obj.contract_util:
            player_data.append(" contract_util:'%s' " % obj.contract_util.strftime('%Y-%m-%d'))
        cypher = "MERGE (pl:Player{id:%d}) " % obj.id + \
                 ("SET pl+={" + ",".join(player_data) + "}") if player_data else ""
        if obj.nationality:
            cypher += " MERGE (nation:Nation{name:'%s'}) MERGE (pl) -[:BORN_IN]-> (nation) " % obj.nationality
        if obj.club:
            cypher += " MERGE (club:Club{name:'%s'}) MERGE (pl) -[:PLAY_FOR]-> (club) " % obj.club.name
        if obj.nation_team:
            cypher += " MERGE (nt:NationTeam{name:'%s'}) MERGE (pl) -[:PLAY_FOR]-> (nt) " % obj.nation_team.name
        tx.run(cypher)

    def add_coach(self, tx, obj):
        coach_data = []
        if obj.name:
            coach_data.append("name:'%s'" % str(obj.name))
        if obj.alias:
            coach_data.append("alias:%s" % str(obj.alias))
        if obj.en_name:
            coach_data.append(" en_name:'%s'" % obj.en_name)
        if obj.nick_name:
            coach_data.append(" nick_name:%s" % obj.nick_name)
        if obj.gender:
            coach_data.append(" gender:'%s'" % obj.get_gender_display())
        if obj.height:
            coach_data.append(" height:%d" % obj.height)
        if obj.birth:
            coach_data.append(" birth:'%s'" % obj.birth.strftime('%Y-%m-%d'))
        if obj.age:
            coach_data.append(" age:%d" % obj.age)
        cypher = "MERGE (coach:Coach{id:%d}) " % obj.id + \
                 ("SET coach+={" + ",".join(coach_data) + "}") if coach_data else ""
        if obj.nationality:
            cypher += " MERGE (nation:Nation{name:'%s'}) MERGE (coach) -[:BORN_IN]-> (nation) " % obj.nationality
        if obj.club:
            cypher += " MERGE (club:Club{name:'%s'}) MERGE (coach) -[:COACH_FOR]-> (club) " % obj.club.name
        if obj.nation_team:
            cypher += " MERGE (nt:NationTeam{name:'%s'}) MERGE (coach) -[:COACH_FOR]-> (nt) " % obj.nation_team.name
        tx.run(cypher)

    def add_match(self, tx, obj):
        pass

    def handle(self, *args, **options):
        self._start_session()
        competition_qs = models.Competition.objects.all()
        club_qs = models.Club.objects.all()
        nation_team_qs = models.NationTeam.objects.all()
        player_qs = models.Player.objects.all()
        coach_qs = models.Coach.objects.all()
        play_record_qs = models.PlayRecord.objects.all()
        coach_record_qs = models.CoachRecord.objects.all()
        match_qs = models.Match.objects.all()
        performance_qs = models.PlayerPerformance.objects.all()
        compe_data_qs = models.CompetitionData.objects.all()

        for q in queryset_iterator(competition_qs):
            print('IMPORT COMPETITION %s' % q.name)
            self.session.write_transaction(self.add_competition, q)

        for q in queryset_iterator(club_qs):
            print('IMPORT CLUB %s' % q.name)
            self.session.write_transaction(self.add_club, q)

        for q in queryset_iterator(nation_team_qs):
            print('IMPORT NATION TEAM %s' % q.name)
            self.session.write_transaction(self.add_nation_team, q)

        for q in queryset_iterator(player_qs):
            print('IMPORT PLAYER %s' % q.name)
            self.session.write_transaction(self.add_player, q)

        # for q in queryset_iterator(coach_qs):
        #     print('IMPORT COACH %s' % q.name)
        #     self.session.write_transaction(self.add_coach, q)

