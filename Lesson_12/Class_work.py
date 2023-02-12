import re

# is_match = re.match(r'380{1}[0-9]{9}', '0678312179')
# print(is_match)

is_replace = re.sub(r'_', ' ', 'a_df_sa')
print(is_replace)