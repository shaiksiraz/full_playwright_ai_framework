import playwright
from playwright._impl._errors import Error
from ai_utils.smart_locator import suggest_locator




class BasePage():
    def __init__ (self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def find_element(self, locator):
        try:
            return self.page.locator(locator).wait_for(state="visible")
        except Error as e:
            suggested_locator = suggest_locator(self.page, locator)
            if suggested_locator:
                return self.page.locator(suggested_locator).nth(0).wait_for(state="visible")
            else:
                raise e

    # def perform_action(self, locator, action, value=None):
    #     if action == 'click':
    #         self.find_element(locator).click()
    #         return
    #     elif action == 'type':
    #         self.find_element(locator).type()
    #     elif action == 'fill':
    #         self.find_element(locator).fill()
    #     elif action == 'clear':
    #         self.find_element(locator).clear()
    #     elif action == 'check':
    #         self.find_element(locator).check()
    #     elif action == 'uncheck':
    #         self.find_element(locator).uncheck()
    #     elif action == 'select_option_by_text':
    #         self.find_element(locator).select_option( value )
    #     elif action == 'select_option_by_index':
    #         self.find_element(locator).select_option_by_index( value )
    #     else:
    #         raise ValueError(f"Unknown action: {action}, implement the action in BasePage")
    def perform_action(self, locator_name, action_name, *args, **kwargs):
        element = self.find_element(locator_name)
        actions = {
            'click': (element.click, lambda: self.page.wait_for_timeout(100)),
            'type': (element.type, lambda: self.page.press("Tab")),
            'fill': element.fill,
            'clear': element.clear,
            'check': element.check,
            'uncheck': element.uncheck,
            'select_option_by_text': element.select_option,
            'hover': element.hover,
            'scroll_to': (lambda: self.page.scroll_to(locator_name)),
            'drag_and_drop': (lambda: self.page.drag_and_drop(locator_name, args[0])),
            'upload_file': (lambda: self.page.upload_file(locator_name, args[0])),
            'download_file': (lambda: self.page.download_file(locator_name, args[0])),
            'switch_to_frame': (lambda: self.page.switch_to_frame(locator_name)),
            'switch_to_window': (lambda: self.page.switch_to_window(locator_name)),
            'dismiss_alert': (lambda: self.page.dismiss_alert()),
            'accept_alert': (lambda: self.page.accept_alert()),
            'execute_script': (lambda: self.page.execute_script(locator_name, args[0])),
            'execute_javascript': (lambda: self.page.execute_javascript(locator_name, args[0])),
        }
        if action_name not in actions:
            raise ValueError(f"Unknown action: {action_name}, implement the action in BasePage")
        if isinstance(actions[action_name], tuple):
            actions[action_name][0](*args, **kwargs)
            actions[action_name][1]()
        else:
            actions[action_name](*args, **kwargs)
