from docutils import nodes
from docutils.parsers.rst import Directive, roles
from sphinx.util.docutils import SphinxDirective

keyword_map = {
    "KEYWORD1": "Replacement1",
    "KEYWORD2": "Replacement2",
    # ... add as many as you want
}

class KeywordReplacerDirective(SphinxDirective):
    has_content = True

    def run(self):
        # Fetch the keyword map from Sphinx's environment
        # keyword_map = self.env.keyword_map

        replaced_content = ' '.join(self.content)
        for key, value in keyword_map.items():
            replaced_content = replaced_content.replace(key, value)

        return [nodes.paragraph(text=replaced_content)]

def keyword_replacer_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    # Fetch the keyword map from Sphinx's environment
    keyword_map = inliner.document.settings.env.config.keyword_map

    for key, value in keyword_map.items():
        text = text.replace(key, value)

    node = nodes.Text(text, text)
    return [node], []

def process_env(app, doctree, fromdocname):
    env = app.builder.env
    env.keyword_map = app.config.keyword_map

def setup(app):
    app.add_config_value('keyword_map', {}, 'html')
    app.connect('doctree-resolved', process_env)
    app.add_directive("replace_keywords", KeywordReplacerDirective)
    roles.register_canonical_role("replace_keywords_inline", keyword_replacer_role)
