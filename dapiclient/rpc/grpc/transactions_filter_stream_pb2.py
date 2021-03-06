# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transactions_filter_stream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transactions_filter_stream.proto',
  package='org.dash.platform.dapi.v0',
  syntax='proto3',
  serialized_pb=_b('\n transactions_filter_stream.proto\x12\x19org.dash.platform.dapi.v0\"\xd3\x01\n\x1dTransactionsWithProofsRequest\x12<\n\x0c\x62loom_filter\x18\x01 \x01(\x0b\x32&.org.dash.platform.dapi.v0.BloomFilter\x12\x19\n\x0f\x66rom_block_hash\x18\x02 \x01(\x0cH\x00\x12\x1b\n\x11\x66rom_block_height\x18\x03 \x01(\rH\x00\x12\r\n\x05\x63ount\x18\x04 \x01(\r\x12\x1f\n\x17send_transaction_hashes\x18\x05 \x01(\x08\x42\x0c\n\nfrom_block\"U\n\x0b\x42loomFilter\x12\x0e\n\x06v_data\x18\x01 \x01(\x0c\x12\x14\n\x0cn_hash_funcs\x18\x02 \x01(\r\x12\x0f\n\x07n_tweak\x18\x03 \x01(\r\x12\x0f\n\x07n_flags\x18\x04 \x01(\r\"\xeb\x01\n\x1eTransactionsWithProofsResponse\x12\x46\n\x10raw_transactions\x18\x01 \x01(\x0b\x32*.org.dash.platform.dapi.v0.RawTransactionsH\x00\x12X\n\x1ainstant_send_lock_messages\x18\x02 \x01(\x0b\x32\x32.org.dash.platform.dapi.v0.InstantSendLockMessagesH\x00\x12\x1a\n\x10raw_merkle_block\x18\x03 \x01(\x0cH\x00\x42\x0b\n\tresponses\"\'\n\x0fRawTransactions\x12\x14\n\x0ctransactions\x18\x01 \x03(\x0c\"+\n\x17InstantSendLockMessages\x12\x10\n\x08messages\x18\x01 \x03(\x0c\x32\xb7\x01\n\x18TransactionsFilterStream\x12\x9a\x01\n!subscribeToTransactionsWithProofs\x12\x38.org.dash.platform.dapi.v0.TransactionsWithProofsRequest\x1a\x39.org.dash.platform.dapi.v0.TransactionsWithProofsResponse0\x01\x62\x06proto3')
)




_TRANSACTIONSWITHPROOFSREQUEST = _descriptor.Descriptor(
  name='TransactionsWithProofsRequest',
  full_name='org.dash.platform.dapi.v0.TransactionsWithProofsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bloom_filter', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsRequest.bloom_filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_block_hash', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsRequest.from_block_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_block_height', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsRequest.from_block_height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsRequest.count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_transaction_hashes', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsRequest.send_transaction_hashes', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='from_block', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsRequest.from_block',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=64,
  serialized_end=275,
)


_BLOOMFILTER = _descriptor.Descriptor(
  name='BloomFilter',
  full_name='org.dash.platform.dapi.v0.BloomFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v_data', full_name='org.dash.platform.dapi.v0.BloomFilter.v_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_hash_funcs', full_name='org.dash.platform.dapi.v0.BloomFilter.n_hash_funcs', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_tweak', full_name='org.dash.platform.dapi.v0.BloomFilter.n_tweak', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_flags', full_name='org.dash.platform.dapi.v0.BloomFilter.n_flags', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=362,
)


_TRANSACTIONSWITHPROOFSRESPONSE = _descriptor.Descriptor(
  name='TransactionsWithProofsResponse',
  full_name='org.dash.platform.dapi.v0.TransactionsWithProofsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_transactions', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsResponse.raw_transactions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instant_send_lock_messages', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsResponse.instant_send_lock_messages', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_merkle_block', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsResponse.raw_merkle_block', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='responses', full_name='org.dash.platform.dapi.v0.TransactionsWithProofsResponse.responses',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=365,
  serialized_end=600,
)


_RAWTRANSACTIONS = _descriptor.Descriptor(
  name='RawTransactions',
  full_name='org.dash.platform.dapi.v0.RawTransactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='org.dash.platform.dapi.v0.RawTransactions.transactions', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=641,
)


_INSTANTSENDLOCKMESSAGES = _descriptor.Descriptor(
  name='InstantSendLockMessages',
  full_name='org.dash.platform.dapi.v0.InstantSendLockMessages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='org.dash.platform.dapi.v0.InstantSendLockMessages.messages', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=643,
  serialized_end=686,
)

_TRANSACTIONSWITHPROOFSREQUEST.fields_by_name['bloom_filter'].message_type = _BLOOMFILTER
_TRANSACTIONSWITHPROOFSREQUEST.oneofs_by_name['from_block'].fields.append(
  _TRANSACTIONSWITHPROOFSREQUEST.fields_by_name['from_block_hash'])
_TRANSACTIONSWITHPROOFSREQUEST.fields_by_name['from_block_hash'].containing_oneof = _TRANSACTIONSWITHPROOFSREQUEST.oneofs_by_name['from_block']
_TRANSACTIONSWITHPROOFSREQUEST.oneofs_by_name['from_block'].fields.append(
  _TRANSACTIONSWITHPROOFSREQUEST.fields_by_name['from_block_height'])
_TRANSACTIONSWITHPROOFSREQUEST.fields_by_name['from_block_height'].containing_oneof = _TRANSACTIONSWITHPROOFSREQUEST.oneofs_by_name['from_block']
_TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['raw_transactions'].message_type = _RAWTRANSACTIONS
_TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['instant_send_lock_messages'].message_type = _INSTANTSENDLOCKMESSAGES
_TRANSACTIONSWITHPROOFSRESPONSE.oneofs_by_name['responses'].fields.append(
  _TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['raw_transactions'])
_TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['raw_transactions'].containing_oneof = _TRANSACTIONSWITHPROOFSRESPONSE.oneofs_by_name['responses']
_TRANSACTIONSWITHPROOFSRESPONSE.oneofs_by_name['responses'].fields.append(
  _TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['instant_send_lock_messages'])
_TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['instant_send_lock_messages'].containing_oneof = _TRANSACTIONSWITHPROOFSRESPONSE.oneofs_by_name['responses']
_TRANSACTIONSWITHPROOFSRESPONSE.oneofs_by_name['responses'].fields.append(
  _TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['raw_merkle_block'])
_TRANSACTIONSWITHPROOFSRESPONSE.fields_by_name['raw_merkle_block'].containing_oneof = _TRANSACTIONSWITHPROOFSRESPONSE.oneofs_by_name['responses']
DESCRIPTOR.message_types_by_name['TransactionsWithProofsRequest'] = _TRANSACTIONSWITHPROOFSREQUEST
DESCRIPTOR.message_types_by_name['BloomFilter'] = _BLOOMFILTER
DESCRIPTOR.message_types_by_name['TransactionsWithProofsResponse'] = _TRANSACTIONSWITHPROOFSRESPONSE
DESCRIPTOR.message_types_by_name['RawTransactions'] = _RAWTRANSACTIONS
DESCRIPTOR.message_types_by_name['InstantSendLockMessages'] = _INSTANTSENDLOCKMESSAGES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionsWithProofsRequest = _reflection.GeneratedProtocolMessageType('TransactionsWithProofsRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONSWITHPROOFSREQUEST,
  __module__ = 'transactions_filter_stream_pb2'
  # @@protoc_insertion_point(class_scope:org.dash.platform.dapi.v0.TransactionsWithProofsRequest)
  ))
_sym_db.RegisterMessage(TransactionsWithProofsRequest)

BloomFilter = _reflection.GeneratedProtocolMessageType('BloomFilter', (_message.Message,), dict(
  DESCRIPTOR = _BLOOMFILTER,
  __module__ = 'transactions_filter_stream_pb2'
  # @@protoc_insertion_point(class_scope:org.dash.platform.dapi.v0.BloomFilter)
  ))
_sym_db.RegisterMessage(BloomFilter)

TransactionsWithProofsResponse = _reflection.GeneratedProtocolMessageType('TransactionsWithProofsResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONSWITHPROOFSRESPONSE,
  __module__ = 'transactions_filter_stream_pb2'
  # @@protoc_insertion_point(class_scope:org.dash.platform.dapi.v0.TransactionsWithProofsResponse)
  ))
_sym_db.RegisterMessage(TransactionsWithProofsResponse)

RawTransactions = _reflection.GeneratedProtocolMessageType('RawTransactions', (_message.Message,), dict(
  DESCRIPTOR = _RAWTRANSACTIONS,
  __module__ = 'transactions_filter_stream_pb2'
  # @@protoc_insertion_point(class_scope:org.dash.platform.dapi.v0.RawTransactions)
  ))
_sym_db.RegisterMessage(RawTransactions)

InstantSendLockMessages = _reflection.GeneratedProtocolMessageType('InstantSendLockMessages', (_message.Message,), dict(
  DESCRIPTOR = _INSTANTSENDLOCKMESSAGES,
  __module__ = 'transactions_filter_stream_pb2'
  # @@protoc_insertion_point(class_scope:org.dash.platform.dapi.v0.InstantSendLockMessages)
  ))
_sym_db.RegisterMessage(InstantSendLockMessages)



_TRANSACTIONSFILTERSTREAM = _descriptor.ServiceDescriptor(
  name='TransactionsFilterStream',
  full_name='org.dash.platform.dapi.v0.TransactionsFilterStream',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=689,
  serialized_end=872,
  methods=[
  _descriptor.MethodDescriptor(
    name='subscribeToTransactionsWithProofs',
    full_name='org.dash.platform.dapi.v0.TransactionsFilterStream.subscribeToTransactionsWithProofs',
    index=0,
    containing_service=None,
    input_type=_TRANSACTIONSWITHPROOFSREQUEST,
    output_type=_TRANSACTIONSWITHPROOFSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSACTIONSFILTERSTREAM)

DESCRIPTOR.services_by_name['TransactionsFilterStream'] = _TRANSACTIONSFILTERSTREAM

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TransactionsFilterStreamStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.subscribeToTransactionsWithProofs = channel.unary_stream(
          '/org.dash.platform.dapi.v0.TransactionsFilterStream/subscribeToTransactionsWithProofs',
          request_serializer=TransactionsWithProofsRequest.SerializeToString,
          response_deserializer=TransactionsWithProofsResponse.FromString,
          )


  class TransactionsFilterStreamServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def subscribeToTransactionsWithProofs(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TransactionsFilterStreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'subscribeToTransactionsWithProofs': grpc.unary_stream_rpc_method_handler(
            servicer.subscribeToTransactionsWithProofs,
            request_deserializer=TransactionsWithProofsRequest.FromString,
            response_serializer=TransactionsWithProofsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'org.dash.platform.dapi.v0.TransactionsFilterStream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTransactionsFilterStreamServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def subscribeToTransactionsWithProofs(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTransactionsFilterStreamStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def subscribeToTransactionsWithProofs(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_TransactionsFilterStream_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('org.dash.platform.dapi.v0.TransactionsFilterStream', 'subscribeToTransactionsWithProofs'): TransactionsWithProofsRequest.FromString,
    }
    response_serializers = {
      ('org.dash.platform.dapi.v0.TransactionsFilterStream', 'subscribeToTransactionsWithProofs'): TransactionsWithProofsResponse.SerializeToString,
    }
    method_implementations = {
      ('org.dash.platform.dapi.v0.TransactionsFilterStream', 'subscribeToTransactionsWithProofs'): face_utilities.unary_stream_inline(servicer.subscribeToTransactionsWithProofs),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_TransactionsFilterStream_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('org.dash.platform.dapi.v0.TransactionsFilterStream', 'subscribeToTransactionsWithProofs'): TransactionsWithProofsRequest.SerializeToString,
    }
    response_deserializers = {
      ('org.dash.platform.dapi.v0.TransactionsFilterStream', 'subscribeToTransactionsWithProofs'): TransactionsWithProofsResponse.FromString,
    }
    cardinalities = {
      'subscribeToTransactionsWithProofs': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'org.dash.platform.dapi.v0.TransactionsFilterStream', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
