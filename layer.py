from yowsup.layers import YowLayer
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity
from yowsup.layers.protocol_presence.protocolentities import PresenceProtocolEntity, AvailablePresenceProtocolEntity, UnavailablePresenceProtocolEntity
from yowsup.layers.protocol_chatstate.protocolentities import OutgoingChatstateProtocolEntity
from yowsup.common.tools import Jid
from yowsup.layers.network import YowNetworkLayer
import time
import random
import os
import sys
import config


class EchoLayer(YowLayer):
  def onLogin(self):
    print("Logged in!")

    name = config.name

    self.toLower(PresenceProtocolEntity(name=name))
    self.online()

  def onEvent(self, yowLayerEvent):
    name = yowLayerEvent.getName()

    if(name == YowNetworkLayer.EVENT_STATE_DISCONNECTED):
      sys.exit(1)

  def receive(self, protocolEntity):
    tag = protocolEntity.getTag()

    if tag == "success":
      self.onLogin()
    elif tag == "failure":
      print("Unauthorized!")
    elif tag == "message":
      self.onMessage(protocolEntity)
    elif tag == "ack":
      self.onAck(protocolEntity)
    elif tag == "receipt":
      self.onReceipt(protocolEntity)

  def onMessage(self, messageProtocolEntity):
    receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), "read", messageProtocolEntity.getParticipant())
    self.toLower(receipt)

    if messageProtocolEntity.getType() == messageProtocolEntity.MESSAGE_TYPE_TEXT:
      self.onTextMessage(messageProtocolEntity)

  def onReceipt(self, entity):
    ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
    self.toLower(ack)

  def onAck(self, entity):
    name = entity.getClass()

    if name == "receipt":
      ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", "receipt", entity._from)
      self.toLower(ack)

  def onTextMessage(self, messageProtocolEntity):
    conversation = messageProtocolEntity.getFrom()
    message = messageProtocolEntity.getBody()

    self.send_message(conversation, message)

  def online(self):
    self.toLower(AvailablePresenceProtocolEntity())

  def offline(self):
    self.toLower(UnavailablePresenceProtocolEntity())

  def start_typing(self, conversation):
    self.toLower(OutgoingChatstateProtocolEntity(
      OutgoingChatstateProtocolEntity.STATE_TYPING,
      Jid.normalize(conversation)
    ))

  def stop_typing(self, conversation):
    self.toLower(OutgoingChatstateProtocolEntity(
      OutgoingChatstateProtocolEntity.STATE_PAUSED,
      Jid.normalize(conversation)
    ))

  def send_message(self, conversation, message):
    if(message != ""):
      outgoingMessageProtocolEntity = TextMessageProtocolEntity(
        message,
        to = conversation
      )

      if os.environ.get("DISABLE_TYPING") != "1":
        try:
          self.start_typing(conversation) # Start typing
          time.sleep(random.uniform(0.5, 1.4)) # Keep state of typing
          self.toLower(outgoingMessageProtocolEntity) # Send a message
          self.stop_typing(conversation) # Stop typing
        except:
          pass

      self.toLower(outgoingMessageProtocolEntity)
