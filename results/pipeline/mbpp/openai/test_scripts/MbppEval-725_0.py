import re

def extract_quotation(text):
    substrings = re.findall(r'"(.*?)"', text)
    extracted_values = [substring.replace('"', '') for substring in substrings]
    return extracted_values

def check(candidate):
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
    assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
    assert extract_quotation("Watch content '4k Ultra HD' resolution with 'HDR 10' Support") == []

check(extract_quotation)