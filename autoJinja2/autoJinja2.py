import sublime
import sublime_plugin
import os


class AutoJinja2Syntax(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        file_abs_path = view.file_name()
        dir_name = os.path.dirname(file_abs_path)
        file_name = os.path.basename(file_abs_path)
        jinja2_syntax = {'Packages/Jinja2/Syntaxes/HTML (Jinja2).tmLanguage',
                         'Packages/Jinja2/Syntaxes/Jinja2.tmLanguage'}

        if 'templates' in dir_name and file_name.endswith('.html'):
            if view.settings().get('syntax') not in jinja2_syntax:
                view.set_syntax_file('Packages/Jinja2/Syntaxes/HTML (Jinja2).tmLanguage')
