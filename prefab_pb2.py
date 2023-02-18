# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prefab.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cprefab.proto\x12\x06prefab\"W\n\x14\x43onfigServicePointer\x12\x12\n\nproject_id\x18\x01 \x01(\x03\x12\x13\n\x0bstart_at_id\x18\x02 \x01(\x03\x12\x16\n\x0eproject_env_id\x18\x03 \x01(\x03\"\xa3\x02\n\x0b\x43onfigValue\x12\r\n\x03int\x18\x01 \x01(\x03H\x00\x12\x10\n\x06string\x18\x02 \x01(\tH\x00\x12\x0f\n\x05\x62ytes\x18\x03 \x01(\x0cH\x00\x12\x10\n\x06\x64ouble\x18\x04 \x01(\x01H\x00\x12\x0e\n\x04\x62ool\x18\x05 \x01(\x08H\x00\x12\x31\n\x0fweighted_values\x18\x06 \x01(\x0b\x32\x16.prefab.WeightedValuesH\x00\x12\x33\n\x10limit_definition\x18\x07 \x01(\x0b\x32\x17.prefab.LimitDefinitionH\x00\x12%\n\tlog_level\x18\t \x01(\x0e\x32\x10.prefab.LogLevelH\x00\x12)\n\x0bstring_list\x18\n \x01(\x0b\x32\x12.prefab.StringListH\x00\x42\x06\n\x04type\"\x1c\n\nStringList\x12\x0e\n\x06values\x18\x01 \x03(\t\"C\n\rWeightedValue\x12\x0e\n\x06weight\x18\x01 \x01(\x05\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.prefab.ConfigValue\"@\n\x0eWeightedValues\x12.\n\x0fweighted_values\x18\x01 \x03(\x0b\x32\x15.prefab.WeightedValue\"h\n\x07\x43onfigs\x12\x1f\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32\x0e.prefab.Config\x12<\n\x16\x63onfig_service_pointer\x18\x02 \x01(\x0b\x32\x1c.prefab.ConfigServicePointer\"\xf7\x01\n\x06\x43onfig\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\nproject_id\x18\x02 \x01(\x03\x12\x0b\n\x03key\x18\x03 \x01(\t\x12%\n\nchanged_by\x18\x04 \x01(\x0b\x32\x11.prefab.ChangedBy\x12\x1f\n\x04rows\x18\x05 \x03(\x0b\x32\x11.prefab.ConfigRow\x12-\n\x10\x61llowable_values\x18\x06 \x03(\x0b\x32\x13.prefab.ConfigValue\x12\'\n\x0b\x63onfig_type\x18\x07 \x01(\x0e\x32\x12.prefab.ConfigType\x12\x14\n\x07\x64raftId\x18\x08 \x01(\x03H\x00\x88\x01\x01\x42\n\n\x08_draftId\"+\n\tChangedBy\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"\xe4\x01\n\tConfigRow\x12\x1b\n\x0eproject_env_id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12(\n\x06values\x18\x02 \x03(\x0b\x32\x18.prefab.ConditionalValue\x12\x35\n\nproperties\x18\x03 \x03(\x0b\x32!.prefab.ConfigRow.PropertiesEntry\x1a\x46\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.prefab.ConfigValue:\x02\x38\x01\x42\x11\n\x0f_project_env_id\"[\n\x10\x43onditionalValue\x12#\n\x08\x63riteria\x18\x01 \x03(\x0b\x32\x11.prefab.Criterion\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.prefab.ConfigValue\"\xdb\x03\n\rLimitResponse\x12\x0e\n\x06passed\x18\x01 \x01(\x08\x12\x12\n\nexpires_at\x18\x02 \x01(\x03\x12\x16\n\x0e\x65nforced_group\x18\x03 \x01(\t\x12\x16\n\x0e\x63urrent_bucket\x18\x04 \x01(\x03\x12\x14\n\x0cpolicy_group\x18\x05 \x01(\t\x12;\n\x0bpolicy_name\x18\x06 \x01(\x0e\x32&.prefab.LimitResponse.LimitPolicyNames\x12\x14\n\x0cpolicy_limit\x18\x07 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x03\x12\x16\n\x0elimit_reset_at\x18\t \x01(\x03\x12\x39\n\x0csafety_level\x18\n \x01(\x0e\x32#.prefab.LimitDefinition.SafetyLevel\"\xa9\x01\n\x10LimitPolicyNames\x12\x0b\n\x07NOT_SET\x10\x00\x12\x14\n\x10SECONDLY_ROLLING\x10\x01\x12\x14\n\x10MINUTELY_ROLLING\x10\x03\x12\x12\n\x0eHOURLY_ROLLING\x10\x05\x12\x11\n\rDAILY_ROLLING\x10\x07\x12\x13\n\x0fMONTHLY_ROLLING\x10\x08\x12\x0c\n\x08INFINITE\x10\t\x12\x12\n\x0eYEARLY_ROLLING\x10\n\"\x99\x02\n\x0cLimitRequest\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x16\n\x0e\x61\x63quire_amount\x18\x02 \x01(\x05\x12\x0e\n\x06groups\x18\x03 \x03(\t\x12:\n\x0elimit_combiner\x18\x04 \x01(\x0e\x32\".prefab.LimitRequest.LimitCombiner\x12\x1e\n\x16\x61llow_partial_response\x18\x05 \x01(\x08\x12\x39\n\x0csafety_level\x18\x06 \x01(\x0e\x32#.prefab.LimitDefinition.SafetyLevel\"6\n\rLimitCombiner\x12\x0b\n\x07NOT_SET\x10\x00\x12\x0b\n\x07MINIMUM\x10\x01\x12\x0b\n\x07MAXIMUM\x10\x02\"\x82\x03\n\tCriterion\x12\x15\n\rproperty_name\x18\x01 \x01(\t\x12\x35\n\x08operator\x18\x02 \x01(\x0e\x32#.prefab.Criterion.CriterionOperator\x12+\n\x0evalue_to_match\x18\x03 \x01(\x0b\x32\x13.prefab.ConfigValue\"\xf9\x01\n\x11\x43riterionOperator\x12\x0b\n\x07NOT_SET\x10\x00\x12\x11\n\rLOOKUP_KEY_IN\x10\x01\x12\x15\n\x11LOOKUP_KEY_NOT_IN\x10\x02\x12\n\n\x06IN_SEG\x10\x03\x12\x0e\n\nNOT_IN_SEG\x10\x04\x12\x0f\n\x0b\x41LWAYS_TRUE\x10\x05\x12\x12\n\x0ePROP_IS_ONE_OF\x10\x06\x12\x16\n\x12PROP_IS_NOT_ONE_OF\x10\x07\x12\x19\n\x15PROP_ENDS_WITH_ONE_OF\x10\x08\x12!\n\x1dPROP_DOES_NOT_END_WITH_ONE_OF\x10\t\x12\x16\n\x12HIERARCHICAL_MATCH\x10\n\"\x93\x01\n\x08Identity\x12\x13\n\x06lookup\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x34\n\nattributes\x18\x02 \x03(\x0b\x32 .prefab.Identity.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07_lookup\"\x89\x01\n\x11\x43lientConfigValue\x12\x10\n\x03int\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x13\n\x06string\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x64ouble\x18\x03 \x01(\x01H\x02\x88\x01\x01\x12\x11\n\x04\x62ool\x18\x04 \x01(\x08H\x03\x88\x01\x01\x42\x06\n\x04_intB\t\n\x07_stringB\t\n\x07_doubleB\x07\n\x05_bool\"\x94\x01\n\x11\x43onfigEvaluations\x12\x35\n\x06values\x18\x01 \x03(\x0b\x32%.prefab.ConfigEvaluations.ValuesEntry\x1aH\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.prefab.ClientConfigValue:\x02\x38\x01\"\xa8\x02\n\x0fLimitDefinition\x12;\n\x0bpolicy_name\x18\x02 \x01(\x0e\x32&.prefab.LimitResponse.LimitPolicyNames\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\r\n\x05\x62urst\x18\x04 \x01(\x05\x12\x12\n\naccount_id\x18\x05 \x01(\x03\x12\x15\n\rlast_modified\x18\x06 \x01(\x03\x12\x12\n\nreturnable\x18\x07 \x01(\x08\x12\x39\n\x0csafety_level\x18\x08 \x01(\x0e\x32#.prefab.LimitDefinition.SafetyLevel\"@\n\x0bSafetyLevel\x12\x0b\n\x07NOT_SET\x10\x00\x12\x12\n\x0eL4_BEST_EFFORT\x10\x04\x12\x10\n\x0cL5_BOMBPROOF\x10\x05\"@\n\x10LimitDefinitions\x12,\n\x0b\x64\x65\x66initions\x18\x01 \x03(\x0b\x32\x17.prefab.LimitDefinition\"\x8a\x01\n\x0f\x42ufferedRequest\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x14\n\x0climit_groups\x18\x05 \x03(\t\x12\x14\n\x0c\x63ontent_type\x18\x06 \x01(\t\x12\x0c\n\x04\x66ifo\x18\x07 \x01(\x08\"\x94\x01\n\x0c\x42\x61tchRequest\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x14\n\x0climit_groups\x18\x05 \x03(\t\x12\x16\n\x0e\x62\x61tch_template\x18\x06 \x01(\t\x12\x17\n\x0f\x62\x61tch_separator\x18\x07 \x01(\t\" \n\rBasicResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"3\n\x10\x43reationResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06new_id\x18\x02 \x01(\x03\"h\n\x07IdBlock\x12\x12\n\nproject_id\x18\x01 \x01(\x03\x12\x16\n\x0eproject_env_id\x18\x02 \x01(\x03\x12\x15\n\rsequence_name\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x03\"a\n\x0eIdBlockRequest\x12\x12\n\nproject_id\x18\x01 \x01(\x03\x12\x16\n\x0eproject_env_id\x18\x02 \x01(\x03\x12\x15\n\rsequence_name\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x03*u\n\nConfigType\x12\x17\n\x13NOT_SET_CONFIG_TYPE\x10\x00\x12\n\n\x06\x43ONFIG\x10\x01\x12\x10\n\x0c\x46\x45\x41TURE_FLAG\x10\x02\x12\r\n\tLOG_LEVEL\x10\x03\x12\x0b\n\x07SEGMENT\x10\x04\x12\x14\n\x10LIMIT_DEFINITION\x10\x05*a\n\x08LogLevel\x12\x15\n\x11NOT_SET_LOG_LEVEL\x10\x00\x12\t\n\x05TRACE\x10\x01\x12\t\n\x05\x44\x45\x42UG\x10\x02\x12\x08\n\x04INFO\x10\x03\x12\x08\n\x04WARN\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x12\t\n\x05\x46\x41TAL\x10\t*G\n\tOnFailure\x12\x0b\n\x07NOT_SET\x10\x00\x12\x10\n\x0cLOG_AND_PASS\x10\x01\x12\x10\n\x0cLOG_AND_FAIL\x10\x02\x12\t\n\x05THROW\x10\x03\x32O\n\x10RateLimitService\x12;\n\nLimitCheck\x12\x14.prefab.LimitRequest\x1a\x15.prefab.LimitResponse\"\x00\x32\xc6\x01\n\rConfigService\x12>\n\tGetConfig\x12\x1c.prefab.ConfigServicePointer\x1a\x0f.prefab.Configs\"\x00\x30\x01\x12?\n\x0cGetAllConfig\x12\x1c.prefab.ConfigServicePointer\x1a\x0f.prefab.Configs\"\x00\x12\x34\n\x06Upsert\x12\x0e.prefab.Config\x1a\x18.prefab.CreationResponse\"\x00\x32\x42\n\tIdService\x12\x35\n\x08GetBlock\x12\x16.prefab.IdBlockRequest\x1a\x0f.prefab.IdBlock\"\x00\x32H\n\rClientService\x12\x37\n\x06GetAll\x12\x10.prefab.Identity\x1a\x19.prefab.ConfigEvaluations\"\x00\x42\x1d\n\x13\x63loud.prefab.domainB\x06Prefabb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'prefab_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023cloud.prefab.domainB\006Prefab'
  _CONFIGROW_PROPERTIESENTRY._options = None
  _CONFIGROW_PROPERTIESENTRY._serialized_options = b'8\001'
  _IDENTITY_ATTRIBUTESENTRY._options = None
  _IDENTITY_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _CONFIGEVALUATIONS_VALUESENTRY._options = None
  _CONFIGEVALUATIONS_VALUESENTRY._serialized_options = b'8\001'
  _CONFIGTYPE._serialized_start=3838
  _CONFIGTYPE._serialized_end=3955
  _LOGLEVEL._serialized_start=3957
  _LOGLEVEL._serialized_end=4054
  _ONFAILURE._serialized_start=4056
  _ONFAILURE._serialized_end=4127
  _CONFIGSERVICEPOINTER._serialized_start=24
  _CONFIGSERVICEPOINTER._serialized_end=111
  _CONFIGVALUE._serialized_start=114
  _CONFIGVALUE._serialized_end=405
  _STRINGLIST._serialized_start=407
  _STRINGLIST._serialized_end=435
  _WEIGHTEDVALUE._serialized_start=437
  _WEIGHTEDVALUE._serialized_end=504
  _WEIGHTEDVALUES._serialized_start=506
  _WEIGHTEDVALUES._serialized_end=570
  _CONFIGS._serialized_start=572
  _CONFIGS._serialized_end=676
  _CONFIG._serialized_start=679
  _CONFIG._serialized_end=926
  _CHANGEDBY._serialized_start=928
  _CHANGEDBY._serialized_end=971
  _CONFIGROW._serialized_start=974
  _CONFIGROW._serialized_end=1202
  _CONFIGROW_PROPERTIESENTRY._serialized_start=1113
  _CONFIGROW_PROPERTIESENTRY._serialized_end=1183
  _CONDITIONALVALUE._serialized_start=1204
  _CONDITIONALVALUE._serialized_end=1295
  _LIMITRESPONSE._serialized_start=1298
  _LIMITRESPONSE._serialized_end=1773
  _LIMITRESPONSE_LIMITPOLICYNAMES._serialized_start=1604
  _LIMITRESPONSE_LIMITPOLICYNAMES._serialized_end=1773
  _LIMITREQUEST._serialized_start=1776
  _LIMITREQUEST._serialized_end=2057
  _LIMITREQUEST_LIMITCOMBINER._serialized_start=2003
  _LIMITREQUEST_LIMITCOMBINER._serialized_end=2057
  _CRITERION._serialized_start=2060
  _CRITERION._serialized_end=2446
  _CRITERION_CRITERIONOPERATOR._serialized_start=2197
  _CRITERION_CRITERIONOPERATOR._serialized_end=2446
  _IDENTITY._serialized_start=2449
  _IDENTITY._serialized_end=2596
  _IDENTITY_ATTRIBUTESENTRY._serialized_start=2536
  _IDENTITY_ATTRIBUTESENTRY._serialized_end=2585
  _CLIENTCONFIGVALUE._serialized_start=2599
  _CLIENTCONFIGVALUE._serialized_end=2736
  _CONFIGEVALUATIONS._serialized_start=2739
  _CONFIGEVALUATIONS._serialized_end=2887
  _CONFIGEVALUATIONS_VALUESENTRY._serialized_start=2815
  _CONFIGEVALUATIONS_VALUESENTRY._serialized_end=2887
  _LIMITDEFINITION._serialized_start=2890
  _LIMITDEFINITION._serialized_end=3186
  _LIMITDEFINITION_SAFETYLEVEL._serialized_start=3122
  _LIMITDEFINITION_SAFETYLEVEL._serialized_end=3186
  _LIMITDEFINITIONS._serialized_start=3188
  _LIMITDEFINITIONS._serialized_end=3252
  _BUFFEREDREQUEST._serialized_start=3255
  _BUFFEREDREQUEST._serialized_end=3393
  _BATCHREQUEST._serialized_start=3396
  _BATCHREQUEST._serialized_end=3544
  _BASICRESPONSE._serialized_start=3546
  _BASICRESPONSE._serialized_end=3578
  _CREATIONRESPONSE._serialized_start=3580
  _CREATIONRESPONSE._serialized_end=3631
  _IDBLOCK._serialized_start=3633
  _IDBLOCK._serialized_end=3737
  _IDBLOCKREQUEST._serialized_start=3739
  _IDBLOCKREQUEST._serialized_end=3836
  _RATELIMITSERVICE._serialized_start=4129
  _RATELIMITSERVICE._serialized_end=4208
  _CONFIGSERVICE._serialized_start=4211
  _CONFIGSERVICE._serialized_end=4409
  _IDSERVICE._serialized_start=4411
  _IDSERVICE._serialized_end=4477
  _CLIENTSERVICE._serialized_start=4479
  _CLIENTSERVICE._serialized_end=4551
# @@protoc_insertion_point(module_scope)
