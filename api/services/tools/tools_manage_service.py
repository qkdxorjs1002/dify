import logging

from core.tools.tool_manager import ToolManager
from services.tools.tools_transform_service import ToolTransformService

logger = logging.getLogger(__name__)


class ToolManageService:
    @staticmethod
    def list_tool_providers(user_id: str, tenant_id: str):
        """
            list tool providers

            :return: the list of tool providers
        """
        providers = ToolManager.user_list_providers(
            user_id, tenant_id
        )

        # add icon
        for provider in providers:
            ToolTransformService.repack_provider(provider)

        result = [provider.to_dict() for provider in providers]

        return result
    