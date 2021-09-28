def singleton(class_):
  """
  Декоратор, представляющий паттерн проектирования "Singleton"
  """
  instances = {}
  def getinstance(*args, **kwargs):
      if class_ not in instances:
          instances[class_] = class_(*args, **kwargs)
      return instances[class_]
  return getinstance