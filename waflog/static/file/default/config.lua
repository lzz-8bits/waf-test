--WAF config file,enable = "on",disable = "off"

--waf status
config_waf_enable = "on"    --开启配置
--log dir
config_log_dir = "/tmp"     --日志地址
--rule setting
config_rule_dir = "/usr/local/openresty/nginx/conf/waf/rule-config" --匹配规则存放地址
--enable/disable white url
config_white_url_check = "on"    --开启url检测
--enable/disable white ip
config_white_ip_check = "on"     --开启ip白名单检测
--enable/disable block ip
config_black_ip_check = "on"     --开启ip黑名单检测
--enable/disable url filtering
config_url_check = "on"          --开启url过滤
--enalbe/disable url args filtering
config_url_args_check = "on"     --开启参数检测
--enable/disable user agent filtering
config_user_agent_check = "on"   --开启ua检测
--enable/disable cookie deny filtering
config_cookie_check = "on"       --开启cookie检测
--enable/disable cc filtering
config_cc_check = "on"           --开启CC检测
--cc rate the xxx of xxx seconds
config_cc_rate = "10/60"         --CC检测 一个ip 60s内最多访问10次
--enable/disable post filtering
config_post_check = "on"         --开启POST检测
--config waf output redirect/html
config_waf_output = "html"       --action返回一个HTML页面
--if config_waf_output ,setting url
config_waf_redirect_url = "https://www.unixhot.com"
config_output_html=[[
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Language" content="zh-cn" />
<title>网站防火墙</title>
</head>
<body>
<h1 align="center"> 欢迎白帽子进行授权安全测试，安全漏洞请联系QQ：1111111。
</body>
</html>
]]

