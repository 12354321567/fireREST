from fireREST import FMC
from json import dumps

# fmc = FMC(hostname='10.106.10.100', username='la-automation', password='#5N4Hcthz40dWdQz0Hd^K!z1rQKsY8$TA3h6ySSKkhV9s4J1ys8BALqArl4P', domain='Global')
fmc = FMC(hostname='10.106.15.51', username='admin', password='LABv2024!!', domain='Global')

# policies = fmc.policy.accesspolicy.get()
# camp_dc_policy = fmc.policy.accesspolicy.accessrule.get(container_name="WPLG-ACP")
# rule = fmc.policy.accesspolicy.accessrule.get(container_name="WPLG-ACP", name="Identity_TEST")

# print(policies)
# print(dumps(camp_dc_policy, indent=2))
# print(dumps(rule, indent=2))


# -------------------------------

# net_objects = fmc.object.network.get()
# network_address = fmc.object.networkaddress.get()
# hosts = fmc.object.host.get()
# network_group = fmc.object.networkgroup.get()

# print(dumps(net_objects, indent=2))
# print(dumps(network_address, indent=2))
# print(dumps(hosts, indent=2))
# print(dumps(network_group, indent=2))



# -------------------------------


# access_list_standard = fmc.object.standardaccesslist.get()
#
# print(dumps(access_list_standard, indent=2))

# -------------------------------

# Example usage:
camp_dc_policy = fmc.policy.accesspolicy.accessrule.get(container_name="WPLG-ACP")
print(camp_dc_policy[0].model_dump_json(indent=2))
# for rule_item in camp_dc_policy:
#     rule = fmc.policy.accesspolicy.accessrule.get(container_name="WPLG-ACP", name=rule_item['name'])
#     print(rule.model_dump_json(indent=2))

rule = fmc.policy.accesspolicy.accessrule.get(container_name="WPLG-ACP", name='TwiceNAT-Test_#4-no-lookup')
print(rule.model_dump_json(indent=2))
