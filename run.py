from yowsup.stacks import YowStackBuilder
from layer import EchoLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env import YowsupEnv
from yowsup.layers.axolotl.props import PROP_IDENTITY_AUTOTRUST
from consonance.structs.keypair import KeyPair
import base64
import sys
import config


credentials = (config.credentials["PHONE"], KeyPair.from_bytes(base64.b64decode(config.credentials["CLIENT_STATIC_KEYPAIR"])))


if __name__==  "__main__":
  stackBuilder = YowStackBuilder()

  try:
    stack = stackBuilder\
      .pushDefaultLayers()\
      .push(EchoLayer)\
      .build()

    stack.setCredentials(credentials)
    stack.setProp(PROP_IDENTITY_AUTOTRUST, True)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT)) # sending the connect signal
    stack.loop()
  except KeyboardInterrupt:
    sys.exit(0)
  except:
    sys.exit(1)
