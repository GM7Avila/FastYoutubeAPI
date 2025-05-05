from pathlib import Path

class AppPaths:
  def __init__(self):
    self.app_dir = Path(__file__).resolve().parent.parent
  
  @property
  def api_dir(self):
    return self.app_dir / "api"
  
  @property
  def core_dir(self):
    return self.app_dir / "core"
  
  @property
  def routes_dir(self):
    return self.app_dir / "routes"
  
  @property
  def services_dir(self):
    return self.app_dir / "services"

# Singleton Instance
app_paths = AppPaths()

# Test
if __name__ == "__main__":
  print(app_paths.app_dir)             # /application
  print(app_paths.api_dir)             # /application/api
  print(app_paths.core_dir)            # /application/core
  print(app_paths.routes_dir)          # /application/routes
  print(app_paths.services_dir)        # /application/services
