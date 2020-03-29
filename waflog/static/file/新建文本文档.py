import os,shutil
node = r'default'

'''def conf_dispaly(node):
    #from waflog.models import Guard
    import re,os
    path = os.path.join('../','file',node)
    print(path)
    if os.path.exists(path):
        print("节点名称 %s 已存在" %(node))
    else:
        os.makedirs(path)   #创建文件夹
        print('节点文件 %s 已创建' %(node))
    conf = open('default/config.lua', 'rb')
    message =conf.readlines()
    for i in message:
        #print(i)

        i = i.decode('UTF-8')
        #config_waf_enable = "on"
        matchObj = re.match(r'(^config_(.*) = "(.*?))" .*',i,re.M|re.I)


        if matchObj:
            if matchObj.group(2) == 'waf_enable':
                print(matchObj.group(2),matchObj.group(3)) #防护类型 开启
            elif matchObj.group(2) == 'white_ip_check':
                print(matchObj.group(2),matchObj.group(3))
            elif matchObj.group(2) == 'black_ip_check':
                print(matchObj.group(2),matchObj.group(3))
            elif matchObj.group(2) == 'url_check':
                print(matchObj.group(2),matchObj.group(3))
            elif matchObj.group(2) == 'user_agent_check':
                print(matchObj.group(2),matchObj.group(3))
            elif matchObj.group(2) == 'cookie_check':
                print(matchObj.group(2),matchObj.group(3))
            elif matchObj.group(2) == 'cc_check':
                print(matchObj.group(2),matchObj.group(3))
            elif matchObj.group(2) == 'waf_output':
                print(matchObj.group(2),matchObj.group(3))
        else:
            print("no match")
    conf.close()
    conf = open('default/config.lua', 'rb')
    guard1 = 'waf_enable'
    txt = conf.read()
    message1 = txt.decode('UTF-8')
    pattern1 = r'((%s+) = "(.*)")'%(guard1)
    matchObj1 = re.search(pattern1,message1,re.M|re.I)

    guard2 = 'waf_output'
    pattern2 = r'((%s+) = "(.*)")'%(guard2)
    matchObj2 = re.search(pattern2,message1,re.M|re.I)
    print('.......................................')
    print(matchObj1.group(2))
    print(matchObj1.group(3))
    print('.......................................')
    print(matchObj2.group(2))
    print(matchObj2.group(3))

    conf.close()

conf_dispaly(node)

node_name = 'cc'
file_dir = os.path.dirname(__file__)
file_path = os.path.join('/file/',node)
path = os.path.join(file_dir,node,r'config.lua')
print(file_dir)
print(file_path)
print(path)
try:
    conf = open(path, 'rb')
    content = conf.read()
    print(content)
    conf.close()
except:
    print("文件路径错误")
#conf.close()

if os.path.exists(file_path):
    print("节点名称 %s 已存在" %(node_name))
else:
    os.makedirs(file_path)   #创建文件夹
    print('节点文件 %s 已创建' %(node_name))'''
def get_MD5(file_path):
    files_md5 = os.popen('md5 %s'%file_path).read().strip()
    file_md5 = files_md5.replace('md5 (%s) = '%file_path,'')
    return file_md5

def copy_file(source_dirname,target_dirname):
    '''for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir,file)
        target_file = os.path.join(target_dir,file)
        if os.path.isfile(source_file):
            if get_MD5(source_file):
                if get_MD5(source_file)!= get_MD5(target_file):
                    shutil.copy(source_file,target_file)

            else:
                shutil.copy(source_file,target_file)
        elif not os.path.isdir()'''
    file_dir = os.path.dirname(__file__)
    source_dir = os.path.join(file_dir,source_dirname)
    target_dir = os.path.join(file_dir,target_dirname)
    print(source_dir)
    print(target_dir)

    if os.path.exists(target_dir):
        print("节点已存在，即将覆盖")
        shutil.rmtree(target_dir)
    shutil.copytree(source_dir,target_dir)


copy_file('default','node1')




