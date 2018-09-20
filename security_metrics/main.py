from security_metrics import utils

csv_path = '../../phishing/parsed_all_phishing_from_9403968.csv'
df = utils.import_csv(csv_path)

print(df['lasttime'])

utils.parser()
