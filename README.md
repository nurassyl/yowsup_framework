**Install**

```bash
./init.sh
```

**Configure**

Get verification code

```bash
# You can see MCC and MNC codes here http://mcc-mnc.com
yowsup-cli registration --config-phone $PHONE_NUMBER_WITH_COUNTRY_CODE --config-cc $COUNTRY_CODE --config-mcc $MCC_CODE --config-mnc $MNC_CODE --requestcode [sms|voice]
```

Get credentials

```bash
# If you get an error, it may means that verification code is invalid or expired, retry again.
yowsup-cli registration --config-phone $PHONE_NUMBER_WITH_COUNTRY_CODE --register $VERIFICATION_CODE
```

Set credentials

```bash
# You can see configuration in ~/.config/yowsup/$PHONE_NUMBER_WITH_COUNTRY_CODE/config.json
cp config_example.py config.py
vim config.py
```

**Fix the error when we send a Whatsapp message to unregistered number**
Issue: https://github.com/tgalal/yowsup/issues/1521#issuecomment-359161584

```bash
./fix.sh
```

**Run**
Note: If you get any error, try it 'yowsup-cli demos --config-phone $PHONE_NUMBER_WITH_COUNTRY_CODE -y' and do command '/L'

```bash
./start.sh

# With disabling typing.
DISABLE_TYPING=1 ./start.sh
```

**You can set settings for your Whatsapp number**

```bash
yowsup-cli demos --config-phone $PHONE_NUMBER_WITH_COUNTRY_CODE -y
```
