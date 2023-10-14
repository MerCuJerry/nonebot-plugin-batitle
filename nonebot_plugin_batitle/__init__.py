from nonebot import on_startswith
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.params import EventPlainText, Startswith
from nonebot.matcher import Matcher
from .draw import draw_pic
from io import BytesIO

__version__ = "0.1.4"
__plugin_meta__ = PluginMetadata(
    name="BlueArchive Title Generator",
    description="碧蓝档案式标题生成器",
    usage="batitle 前|后",
    type="application",
    homepage="https://github.com/MerCuJerry/nonebot-plugin-batitle",
    config=None,
    supported_adapters={"~onebot.v11"},
)

batitle = ("batitle ", "ba标题 ")
batitle_matcher = on_startswith(msg=batitle, block=True, priority=5)


@batitle_matcher.handle()
async def _handler(
    matcher: Matcher, str_match: str = Startswith(), key: str = EventPlainText()
):
    try:
        keyword: str = key.replace(str_match, "")
        if "｜" in keyword:
            keyword = keyword.replace("｜", "|")
        upper = keyword.split("|")[0].strip()
        downer = keyword.split("|")[1].strip()
        img_raw = draw_pic(front=upper, back=downer)
        img = BytesIO()
        img_raw.save(img, format="png")
        img_bytes: bytes = img.getvalue()
        img_raw.close()
        img.close()
        await matcher.finish(MessageSegment.image(img_bytes))

    except OSError:
        await matcher.finish("生成失败……请检查字体文件设置是否正确")
    except IndexError:
        await matcher.finish("生成失败……请检查命令格式是否正确")
