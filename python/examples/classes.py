class Website:
  # constructor
  def __init__(self, url, founding_year, free_to_use):
    self.url = url
    self.founding_year = founding_year
    self.free_to_use = free_to_use
  # method
  def info(self):
    print("URL:", self.url)
    print("Founding year:", self.founding_year)
    print("Free to use:", self.free_to_use)

Website.is_online = True

github = Website('https://github.com/', 2008, True)
github.info()

print("Class attribute (is_online):", Website.is_online)