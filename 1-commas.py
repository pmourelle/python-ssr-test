import locale

locale.setlocale(locale.LC_ALL, 'en_US')


def thousands_with_commas(i):
    ''' Using locale to format number.
        In this case using US' dot as comma thousand separator.
    '''
    return locale.format("%d", i, grouping=True)


if __name__ == '__main__':
    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
    print('Asserts passed')
