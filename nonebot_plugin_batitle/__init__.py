from nonebot import require, get_plugin_config
from nonebot.plugin import PluginMetadata, inherit_supported_adapters
from .draw import draw_pic
from io import BytesIO
from pydantic import BaseModel, Field
from arclet.alconna import Alconna, CommandMeta, Args
from nepattern import AnyString
require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import on_alconna, Match, AlconnaMatch, AlconnaMatcher  # noqa: E402
from nonebot_plugin_alconna.uniseg import UniMessage, Image, Reply, get_message_id  # noqa: E402

class BAGenConfig(BaseModel):
    separator: str = Field(default='|', alias="batitle_generator_separator", description="碧蓝档案式标题生成器参数使用的分隔符")

__version__ = "0.2.1.post1"
__plugin_meta__ = PluginMetadata(
    name="BlueArchive Title Generator",
    description="碧蓝档案式标题生成器",
    usage="batitle 前|后",
    type="application",
    homepage="https://github.com/MerCuJerry/nonebot-plugin-batitle",
    config=BAGenConfig,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={
        "version": __version__,
        "author": "MerCuJerry <mercujerry@gmail.com>",
    },
)

batitle_generator_config: BAGenConfig = get_plugin_config(BAGenConfig)

batitle_matcher = on_alconna(
    Alconna(
        ["batitle", "ba标题"],
        Args["upper", AnyString]["lower", AnyString]
            .separate(batitle_generator_config.separator),
            meta=CommandMeta(description="生成一个碧蓝档案式的标题")
    ),
    block=True,
    priority=5
)

@batitle_matcher.handle()
async def _handler(
    matcher: AlconnaMatcher, 
    upper: Match[str] = AlconnaMatch("upper"),
    lower: Match[str] = AlconnaMatch("lower")):
    try:
        img_raw = draw_pic(front=upper.result, back=lower.result)
        img = BytesIO()
        img_raw.save(img, format="png")
        img_bytes: bytes = img.getvalue()
        img_raw.close()
        img.close()
        await matcher.finish(await UniMessage([Reply(get_message_id()), Image(raw=img_bytes)]).export())

    except OSError:
        await matcher.finish("生成失败……请检查字体文件设置是否正确")
    except IndexError:
        await matcher.finish("生成失败……请检查命令格式是否正确")
