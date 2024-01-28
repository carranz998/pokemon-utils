from data_warehouse.repositories import Type_Chart_Repository

attack_efectiveness = Type_Chart_Repository \
    .get_attack_efectiveness('Fire')

defense_efectivess = Type_Chart_Repository \
    .get_defensive_efectiveness(['Dark', 'Ghost'])

print(attack_efectiveness)
print(defense_efectivess)
