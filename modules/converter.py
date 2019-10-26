alph = {
    'а': 'a',
    'ә': 'á',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'ғ': 'ǵ',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'j',
    'з': 'z',
    'и': 'ı',
    'й': 'ı',
    'к': 'k',
    'қ': 'q',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'ң': 'ń',
    'о': 'o',
    'ө': 'ó',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'ý',
    'ұ': 'u',
    'ү': 'ú',
    'ф': 'f',
    'х': 'h',
    'һ': 'h',
    'ц': 's',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sh',
    'ъ': '',
    'ы': 'y',
    'і': 'i',
    'ь': '',
    'э': 'e',
    'ю': 'ıý',
    'я': 'ıa',
}

ALPH = {}

for a in alph:
  ALPH[a.upper()] = alph[a].upper()

alph.update(ALPH)
del ALPH


def convert(message):
  new_message = ''

  for a in message:
    try:
      new_message += alph[a]
    except KeyError:
      new_message += a

  return new_message
