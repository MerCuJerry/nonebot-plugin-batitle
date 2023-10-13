<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-batitle

_✨ NoneBot 插件 碧蓝档案式标题生成器✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/MerCuJerry/nonebot-plugin-batitle.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-batitle">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-batitle.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-batitle

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-batitle
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-batitle
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-batitle
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-batitle
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_batitle"]

</details>

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| batitle (前)|(后)| 群员 | 否 | 群聊 | 使用时去掉括号 |
| ba标题 (前)|(后) | 群员 | 否 | 群聊 | 同上 |