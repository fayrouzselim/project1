import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

env = Environment(loader=FileSystemLoader("."))

print("Welcome to Router Configuration Script!")
preference = input("Enter your preference (BGP, OSPF, or static routing): ").lower()
if preference == "bgp":
    as_number = input("Enter your AS number: ")
    router_id = input("Enter your Router ID: ")
    neighbor_ip = input("Enter neighbor IP address: ")
    neighbor_as = input("Enter neighbor AS number: ")
    with open("bgp.yaml", "w") as bgp_yaml:
        yaml.dump({"as_number": as_number, "router_id": router_id, "neighbor_ip": neighbor_ip, "neighbor_as": neighbor_as}, bgp_yaml)
    with open("bgp.yaml") as bgp_file:
        data = yaml.full_load(bgp_file)
    print(data)
    template = env.get_template('bgp.j2')
    rendered_template = template.render(int=data)
    print(rendered_template)
elif preference == "ospf":
    process_id = input("Enter process ID: ")
    router_id = input("Enter your Router ID: ")
    network_address = input("Enter network IP address: ")
    wild_card_mask = input("Enter wild card mask: ")
    area_id = input("Enter area id: ")
    with open("ospf.yaml", "w") as ospf_yaml:
        yaml.dump({"process_id": process_id, "router_id": router_id, "network_address": network_address, "wild_card_mask": wild_card_mask, "area_id": area_id}, ospf_yaml)
    with open("ospf.yaml") as ospf_file:
        data = yaml.full_load(ospf_file)
    print(data)
    template = env.get_template('ospf.j2')
    rendered_template = template.render(int=data)
    print(rendered_template)
elif preference == "static":
    destination_network = input("Enter the destination network: ")
    subnet_mask = input("Enter the network subnet mask: ")
    exit_interface = input("Enter the exit interface: ")
    with open("static.yaml", "w") as static_yaml:
        yaml.dump({"destination_network": destination_network, "subnet_mask": subnet_mask, "exit_interface": exit_interface}, static_yaml)
    with open("static.yaml") as static_file:
        data = yaml.full_load(static_file)
    print(data)
    template = env.get_template('static.j2')
    rendered_template = template.render(int=data)
    print(rendered_template)
else:
    print("Invalid preference. Please choose BGP, OSPF, or static routing.")

router_model = input("Enter router model for ssh: ")
router_ip = input("Enter router IP for ssh: ")
router_user_name = input("Enter router user name for ssh: ")
router_password = input("Enter router password for ssh: ")
device = {
    'device_type': router_model,
    'host': router_ip,
    'username': router_user_name,
    'password': router_password,
}

try:

    net_connect = ConnectHandler(**device)

    output1 = net_connect.send_command("show ip interface brief")

    output2 = net_connect.send_config_set(rendered_template)

    net_connect.disconnect()

except Exception as e:
    print("An error occurred:", str(e))

C

A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B

