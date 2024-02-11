# mypy: disable-error-code="assignment"
# flake8: noqa: E401

# Overriding the original models with the ones in the upbank_spec package
from upbank_client.models.money_object import MoneyObject

# BEGIN ORIGINAL TYPES
# import models into model package
from upbank_spec.models.account_resource import AccountResource
from upbank_spec.models.account_resource_attributes import AccountResourceAttributes
from upbank_spec.models.account_resource_links import AccountResourceLinks
from upbank_spec.models.account_resource_relationships import AccountResourceRelationships
from upbank_spec.models.account_resource_relationships_transactions import AccountResourceRelationshipsTransactions
from upbank_spec.models.account_resource_relationships_transactions_links import AccountResourceRelationshipsTransactionsLinks
from upbank_spec.models.account_type_enum import AccountTypeEnum
from upbank_spec.models.cashback_object import CashbackObject
from upbank_spec.models.category_input_resource_identifier import CategoryInputResourceIdentifier
from upbank_spec.models.category_resource import CategoryResource
from upbank_spec.models.category_resource_attributes import CategoryResourceAttributes
from upbank_spec.models.category_resource_relationships import CategoryResourceRelationships
from upbank_spec.models.category_resource_relationships_children import CategoryResourceRelationshipsChildren
from upbank_spec.models.category_resource_relationships_children_data_inner import CategoryResourceRelationshipsChildrenDataInner
from upbank_spec.models.category_resource_relationships_parent import CategoryResourceRelationshipsParent
from upbank_spec.models.category_resource_relationships_parent_data import CategoryResourceRelationshipsParentData
from upbank_spec.models.create_webhook_request import CreateWebhookRequest
from upbank_spec.models.create_webhook_response import CreateWebhookResponse
from upbank_spec.models.error_object import ErrorObject
from upbank_spec.models.error_object_source import ErrorObjectSource
from upbank_spec.models.error_response import ErrorResponse
from upbank_spec.models.get_account_response import GetAccountResponse
from upbank_spec.models.get_category_response import GetCategoryResponse
from upbank_spec.models.get_transaction_response import GetTransactionResponse
from upbank_spec.models.get_webhook_response import GetWebhookResponse
from upbank_spec.models.hold_info_object import HoldInfoObject
from upbank_spec.models.hold_info_object_foreign_amount import HoldInfoObjectForeignAmount
from upbank_spec.models.list_accounts_response import ListAccountsResponse
from upbank_spec.models.list_accounts_response_links import ListAccountsResponseLinks
from upbank_spec.models.list_categories_response import ListCategoriesResponse
from upbank_spec.models.list_tags_response import ListTagsResponse
from upbank_spec.models.list_transactions_response import ListTransactionsResponse
from upbank_spec.models.list_webhook_delivery_logs_response import ListWebhookDeliveryLogsResponse
from upbank_spec.models.list_webhooks_response import ListWebhooksResponse
from upbank_spec.models.money_object import MoneyObject
from upbank_spec.models.ownership_type_enum import OwnershipTypeEnum
from upbank_spec.models.ping_response import PingResponse
from upbank_spec.models.ping_response_meta import PingResponseMeta
from upbank_spec.models.round_up_object import RoundUpObject
from upbank_spec.models.round_up_object_boost_portion import RoundUpObjectBoostPortion
from upbank_spec.models.tag_input_resource_identifier import TagInputResourceIdentifier
from upbank_spec.models.tag_resource import TagResource
from upbank_spec.models.transaction_resource import TransactionResource
from upbank_spec.models.transaction_resource_attributes import TransactionResourceAttributes
from upbank_spec.models.transaction_resource_attributes_cashback import TransactionResourceAttributesCashback
from upbank_spec.models.transaction_resource_attributes_foreign_amount import TransactionResourceAttributesForeignAmount
from upbank_spec.models.transaction_resource_attributes_hold_info import TransactionResourceAttributesHoldInfo
from upbank_spec.models.transaction_resource_attributes_round_up import TransactionResourceAttributesRoundUp
from upbank_spec.models.transaction_resource_relationships import TransactionResourceRelationships
from upbank_spec.models.transaction_resource_relationships_account import TransactionResourceRelationshipsAccount
from upbank_spec.models.transaction_resource_relationships_account_data import TransactionResourceRelationshipsAccountData
from upbank_spec.models.transaction_resource_relationships_category import TransactionResourceRelationshipsCategory
from upbank_spec.models.transaction_resource_relationships_category_links import TransactionResourceRelationshipsCategoryLinks
from upbank_spec.models.transaction_resource_relationships_tags import TransactionResourceRelationshipsTags
from upbank_spec.models.transaction_resource_relationships_tags_data_inner import TransactionResourceRelationshipsTagsDataInner
from upbank_spec.models.transaction_resource_relationships_tags_links import TransactionResourceRelationshipsTagsLinks
from upbank_spec.models.transaction_resource_relationships_transfer_account import TransactionResourceRelationshipsTransferAccount
from upbank_spec.models.transaction_resource_relationships_transfer_account_data import TransactionResourceRelationshipsTransferAccountData
from upbank_spec.models.transaction_status_enum import TransactionStatusEnum
from upbank_spec.models.update_transaction_category_request import UpdateTransactionCategoryRequest
from upbank_spec.models.update_transaction_category_request_data import UpdateTransactionCategoryRequestData
from upbank_spec.models.update_transaction_tags_request import UpdateTransactionTagsRequest
from upbank_spec.models.webhook_delivery_log_resource import WebhookDeliveryLogResource
from upbank_spec.models.webhook_delivery_log_resource_attributes import WebhookDeliveryLogResourceAttributes
from upbank_spec.models.webhook_delivery_log_resource_attributes_request import WebhookDeliveryLogResourceAttributesRequest
from upbank_spec.models.webhook_delivery_log_resource_attributes_response import WebhookDeliveryLogResourceAttributesResponse
from upbank_spec.models.webhook_delivery_log_resource_relationships import WebhookDeliveryLogResourceRelationships
from upbank_spec.models.webhook_delivery_log_resource_relationships_webhook_event import WebhookDeliveryLogResourceRelationshipsWebhookEvent
from upbank_spec.models.webhook_delivery_log_resource_relationships_webhook_event_data import WebhookDeliveryLogResourceRelationshipsWebhookEventData
from upbank_spec.models.webhook_delivery_status_enum import WebhookDeliveryStatusEnum
from upbank_spec.models.webhook_event_callback import WebhookEventCallback
from upbank_spec.models.webhook_event_resource import WebhookEventResource
from upbank_spec.models.webhook_event_resource_attributes import WebhookEventResourceAttributes
from upbank_spec.models.webhook_event_resource_relationships import WebhookEventResourceRelationships
from upbank_spec.models.webhook_event_resource_relationships_transaction import WebhookEventResourceRelationshipsTransaction
from upbank_spec.models.webhook_event_resource_relationships_transaction_data import WebhookEventResourceRelationshipsTransactionData
from upbank_spec.models.webhook_event_resource_relationships_webhook import WebhookEventResourceRelationshipsWebhook
from upbank_spec.models.webhook_event_resource_relationships_webhook_data import WebhookEventResourceRelationshipsWebhookData
from upbank_spec.models.webhook_event_type_enum import WebhookEventTypeEnum
from upbank_spec.models.webhook_input_resource import WebhookInputResource
from upbank_spec.models.webhook_input_resource_attributes import WebhookInputResourceAttributes
from upbank_spec.models.webhook_resource import WebhookResource
from upbank_spec.models.webhook_resource_attributes import WebhookResourceAttributes
from upbank_spec.models.webhook_resource_relationships import WebhookResourceRelationships
# END ORIGINAL TYPES
