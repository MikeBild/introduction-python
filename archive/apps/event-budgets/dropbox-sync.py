import dropbox
import schedule
import sys
import os

dbx = dropbox.Dropbox(os.getenv('DROPBOX_TOKEN'))

def job():
  files = dbx.files_list_folder('/python-in-a-nutshell-data')
  for f in [f.path_lower for f in files.entries]:
    dbx.files_download_to_file('.' + f, f)
    print('Synced file:', f)

schedule.every(5).seconds.do(job)

while True:
  try:
    schedule.run_pending()
  except (KeyboardInterrupt, SystemExit):
    print('Exiting')
    sys.exit()