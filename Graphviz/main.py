import json
import os

basestring = 'digraph{\n' \
             'ratio=0.6;\n' \
             'rankdir = LR;' \
             'node [shape=box; fontsize = 16; label = ""];\n'


# 'size = \"40,20\";' \
def add_node(full_name):
    global basestring
    basestring += '\"' + full_name + '\"'
    if full_name == 'External':
        basestring += '[shape = ellipse]'
    basestring += ';\n'


def add_edge(caller, callee, label):
    global basestring
    basestring += '\"' + caller + '\" -> \"' + callee + '\" [label=\"' + label + '\"];\n'


def add_edge_without_label(caller, callee, label):
    global basestring
    basestring += '\"' + caller + '\" -> \"' + callee + '\"'
    if callee == 'External':
        basestring += '[color=\"#d95f0e\", style = dashed]'
    elif label.__contains__("tcp"):
        basestring += '[color=\"#08519c\"]'
    basestring += ';\n'


if __name__ == '__main__':
    this_time = 4
    apps = ['bookinfo', 'hipstershop', 'sockshop', 'pitstop', 'sitewhere']
    app = apps[this_time]
    for root, dirs, files in os.walk(r"manifest_files/" + app):
        for file_name in files:
            if file_name == '.DS_Store':
                continue
            manifest_file = json.load(open(os.path.join(root, file_name), 'r'))
            full_name = manifest_file['service'] + '-' + manifest_file['version']
            add_node(full_name)

        for file_name in files:
            if file_name == '.DS_Store':
                continue
            manifest_file = json.load(open(os.path.join(root, file_name), 'r'))
            full_name = manifest_file['service'] + '-' + manifest_file['version']
            for request in manifest_file['requests']:
                if request['name'] != '':
                    callee = request['name'] + '-' + manifest_file['version']
                    if request['type'] == 'http':
                        add_edge_without_label(full_name, callee,
                                               label='http, ' + request['path'] + ', ' + request['method'])
                    if request['type'] == 'grpc':
                        add_edge_without_label(full_name, callee, label='grpc, ' + request['path'])
                    if request['type'] == 'tcp':
                        tcp_callee = request['name']
                        add_edge_without_label(full_name, tcp_callee, label='tcp, ' + str(request['port']))
                else:
                    add_node('External')
                    add_edge_without_label(full_name, 'External', label=request['url'] + ', ' + request['method'])
    basestring = basestring + '}'
    print(basestring)

    file = open(app + '.gv', 'w+')
    file.write(basestring)
    file.close()
    os.system('dot ' + app + '.gv -Teps -o ' + app + '.eps')
    # print(root)
    # print(os.path.join(root, file))
