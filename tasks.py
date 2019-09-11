#print("20190515 a")
from atelier.invlib import setup_from_tasks

cfg = dict()
cfg.update(tolerate_sphinx_warnings=True)
# cfg.update(blog_root='/home/luc/work/lutsu/')
cfg.update(languages=['en'])
cfg.update(doc_trees=['docs'])
cfg.update(revision_control_system='git')

#print("20190515 b", cfg)

ns = setup_from_tasks(globals(), **cfg)
# ns.configure(cfg)

#print("20190515 c", cfg)
