#python_respo.py
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


#执行api调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)


#将api响应存储到一个变量中
response_dict = r.json()
print("Total:",response_dict["total_count"])


#探索有关仓库的信息
repo_dicts = response_dict["items"]
print("Items Count:",len(repo_dicts))

#研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# # for key in sorted(repo_dict.keys()):
# # 	print(key)

# print("Ower:",repo_dict["owner"]["login"])

# #处理结果
# print(response_dict.keys())


# print("\n Selected information about each repository")

# for repo_dict in repo_dicts:
# 	print("\nName:",repo_dict["name"])
# 	print("Owner:",repo_dict["owner"]["login"])
# 	print("Star:",repo_dict["stargazers_count"])
# 	print("respository:",repo_dict["html_url"])
# 	print("Description:",str(repo_dict["description"]).encode("utf-8"))



names,plot_dicts= [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict["name"])
	# stars.append(repo_dict["stargazers_count"])
	plot_dict = {
		"value":repo_dict["stargazers_count"],
		"label":str(repo_dict["description"]).encode("utf-8"),
		"xlink":repo_dict["html_url"],
	}
	plot_dicts.append(plot_dict)


#可视化
my_style = LS("#333366",base_style = LCS)
# chart = pygal.Bar(style = my_style,x_label_rotation= 45, show_legend = False)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 24
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config,style = my_style)


chart.title = "Most-starred Python Projects on Github"
chart.x_labels = names

chart.add("",plot_dicts)
chart.render_to_file("python_repos.svg")






















