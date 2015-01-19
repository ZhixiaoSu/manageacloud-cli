from prettytable import PrettyTable


def show_instances(instances):
    pretty = PrettyTable(["Instance name", "Instance ID", "Type", "Status"])

    if (len(instances)):
        for instance in instances:
            pretty.add_row([instance['servername'], instance['id'], instance['type'], instance['status']])
        print(pretty)
    else:
        print("There is no active instances")


def show_instance(instance):
    pretty = PrettyTable(["Instance name", "Instance ID", "Type", "Status"])
    pretty.add_row([instance['servername'], instance['id'], instance['type'], instance['status']])
    print(pretty)


def show_instance_create_locations_example(cookbook_tag, locationid):
    print("")
    print("Example:")
    print("")
    print("    mac instance create -c %s -l %s" % (cookbook_tag, locationid))
    print("")


def show_instance_create_help():
    print("--configuration parameter is required. ")
    print("")
    print("You can list your configurations:")
    print("")
    print("    mac configuration list")
    print("")
    print("or search public configurations")
    print("")
    print("    mac configuration search")
    print("")
    print("To create a new instance with this configuration:")
    print("")
    print("    mac instance create -c <configuration tag>")
    show_instance_help()


def show_instance_help():
    print("")
    print("Show more help:")
    print("")
    print("    mac instance -h")
    print("")


def show_instance_destroy_help():
    print("")
    print("Show more help:")
    print("")
    print("    mac instance destroy -h")
    print("")


def show_instance_ssh_help():
    print("")
    print("Show more help:")
    print("")
    print("    mac instance ssh -h")
    print("")


def show_create_example_with_parameters(cookbook_tag, deployment, location, servername, provider, release, branch,
                                        hardware):
    output = "mac instance create "

    if cookbook_tag is not None and cookbook_tag != "":
        output += " -c " + cookbook_tag

    if deployment is not None and deployment != "testing":
        output += " -d " + deployment

    if location is not None and location != "":
        output += " -l " + location

    if servername is not None and servername != "":
        output += " -n " + servername

    if provider is not None and provider != "manageacloud":
        output += " -p " + provider

    if release is not None and release != "any":
        output += " -r " + release

    if branch is not None and branch != "master":
        output += " -r " + branch

    if hardware is not None and hardware != "":
        output += " -hw " + hardware

    print("")
    print("Example:")
    print("")
    print("    %s" % output)
    print("")