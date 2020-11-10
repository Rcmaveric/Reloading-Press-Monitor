try:
    import tkinter as tk
except:
    import Tkinter as tk


class Demo(tk.LabelFrame):
    """
    A LabeFrame that in order to demonstrate the string returned by the
    get method of Text widget, selects the characters in between the
    given arguments that are set with Scales.
    """

    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)
        self.start_arg = ''
        self.end_arg = None
        self.position_frames = dict()
        self._create_widgets()
        self._layout()
        self.update()


    def _create_widgets(self):
        self._is_two_args = tk.Checkbutton(self,
                                    text="Use 2 positional arguments...")
        self.position_frames['start'] = PositionFrame(self,
                                    text="start='{}.{}'.format(line, column)")
        self.position_frames['end'] = PositionFrame(   self,
                                    text="end='{}.{}'.format(line, column)")
        self.text = TextWithStats(self, wrap='none')
        self._widget_configs()


    def _widget_configs(self):
        self.text.update_callback = self.update
        self._is_two_args.var = tk.BooleanVar(self, value=False)
        self._is_two_args.config(variable=self._is_two_args.var,
                                    onvalue=True, offvalue=False)
        self._is_two_args['command'] = self._is_two_args_handle
        for _key in self.position_frames:
            self.position_frames[_key].line.slider['command'] = self.update
            self.position_frames[_key].column.slider['command'] = self.update


    def _layout(self):
        self._is_two_args.grid(sticky='nsw', row=0, column=1)
        self.position_frames['start'].grid(sticky='nsew', row=1, column=0)
        #self.position_frames['end'].grid(sticky='nsew', row=1, column=1)
        self.text.grid(sticky='nsew', row=2, column=0,
                                                    rowspan=2, columnspan=2)
        _grid_size = self.grid_size()
        for _col in range(_grid_size[0]):
            self.grid_columnconfigure(_col, weight=1)
        for _row in range(_grid_size[1] - 1):
            self.grid_rowconfigure(_row + 1, weight=1)


    def _is_two_args_handle(self):
        self.update_arguments()
        if self._is_two_args.var.get():
            self.position_frames['end'].grid(sticky='nsew', row=1, column=1)
        else:
            self.position_frames['end'].grid_remove()


    def update(self, event=None):
        """
        Updates slider limits, argument values, labels representing the
        get method call.
        """

        self.update_sliders()
        self.update_arguments()


    def update_sliders(self):
        """
        Updates slider limits based on what's written in the text and
        which line is selected.
        """

        self._update_line_sliders()
        self._update_column_sliders()


    def _update_line_sliders(self):
        if self.text.lines_length:
            for _key in self.position_frames:
                self.position_frames[_key].line.slider['state'] = 'normal'
                self.position_frames[_key].line.slider['from_'] = 1
                _no_of_lines = self.text.line_count
                self.position_frames[_key].line.slider['to'] = _no_of_lines
        else:
            for _key in self.position_frames:
                self.position_frames[_key].line.slider['state'] = 'disabled'


    def _update_column_sliders(self):
        if self.text.lines_length:
            for _key in self.position_frames:
                self.position_frames[_key].column.slider['state'] = 'normal'
                self.position_frames[_key].column.slider['from_'] = 0
                _line_no = int(self.position_frames[_key].line.slider.get())-1
                _max_line_len = self.text.lines_length[_line_no]
                self.position_frames[_key].column.slider['to'] = _max_line_len
        else:
            for _key in self.position_frames:
                self.position_frames[_key].column.slider['state'] = 'disabled'


    def update_arguments(self):
        """
        Updates the values representing the arguments passed to the get
        method, based on whether or not the 2nd positional argument is
        active and the slider positions.
        """

        _start_line_no = self.position_frames['start'].line.slider.get()
        _start_col_no = self.position_frames['start'].column.slider.get()
        self.start_arg = "{}.{}".format(_start_line_no, _start_col_no)
        if self._is_two_args.var.get():
            _end_line_no = self.position_frames['end'].line.slider.get()
            _end_col_no = self.position_frames['end'].column.slider.get()
            self.end_arg = "{}.{}".format(_end_line_no, _end_col_no)
        else:
            self.end_arg = None
        self._update_method_labels()
        self._select()


    def _update_method_labels(self):
        if self.end_arg:
            for _key in self.position_frames:
                _string = "text.get('{}', '{}')".format(
                                                self.start_arg, self.end_arg)
                self.position_frames[_key].label['text'] = _string
        else:
            _string = "text.get('{}')".format(self.start_arg)
            self.position_frames['start'].label['text'] = _string


    def _select(self):
        self.text.focus_set()
        self.text.tag_remove('sel', '1.0', 'end')
        self.text.tag_add('sel', self.start_arg, self.end_arg)
        if self.end_arg:
            self.text.mark_set('insert', self.end_arg)
        else:
            self.text.mark_set('insert', self.start_arg)


class TextWithStats(tk.Text):
    """
    Text widget that stores stats of its content:
    self.line_count:        the total number of lines
    self.lines_length:      the total number of characters per line
    self.update_callback:   can be set as the reference to the callback
                            to be called with each update
    """

    def __init__(self, master, update_callback=None, *args, **kwargs):
        tk.Text.__init__(self, master, *args, **kwargs)
        self._events = ('<KeyPress>',
                        '<KeyRelease>',
                        '<ButtonRelease-1>',
                        '<ButtonRelease-2>',
                        '<ButtonRelease-3>',
                        '<Delete>',
                        '<<Cut>>',
                        '<<Paste>>',
                        '<<Undo>>',
                        '<<Redo>>')
        self.line_count = None
        self.lines_length = list()
        self.update_callback = update_callback
        self.update_stats()
        self.bind_events_on_widget_to_callback( self._events,
                                                self,
                                                self.update_stats)


    @staticmethod
    def bind_events_on_widget_to_callback(events, widget, callback):
        """
        Bind events on widget to callback.
        """

        for _event in events:
            widget.bind(_event, callback)


    def update_stats(self, event=None):
        """
        Update self.line_count, self.lines_length stats and call
        self.update_callback.
        """

        _string = self.get('1.0', 'end-1c')
        _string_lines = _string.splitlines()
        self.line_count = len(_string_lines)
        del self.lines_length[:]
        for _line in _string_lines:
            self.lines_length.append(len(_line))
        if self.update_callback:
            self.update_callback()


class PositionFrame(tk.LabelFrame):
    """
    A LabelFrame that has two LabelFrames which has Scales.
    """

    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)
        self._create_widgets()
        self._layout()


    def _create_widgets(self):
        self.line = SliderFrame(self, orient='vertical', text="line=")
        self.column = SliderFrame(self, orient='horizontal', text="column=")
        self.label = tk.Label(self, text="Label")


    def _layout(self):
        self.line.grid(sticky='ns', row=0, column=0, rowspan=2)
        self.column.grid(sticky='ew', row=0, column=1, columnspan=2)
        self.label.grid(sticky='nsew', row=1, column=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)


class SliderFrame(tk.LabelFrame):
    """
    A LabelFrame that encapsulates a Scale.
    """

    def __init__(self, master, orient, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.slider = tk.Scale(self, orient=orient)
        self.slider.pack(fill='both', expand=True)


if __name__ == '__main__':
    root = tk.Tk()
    demo = Demo(root, text="text.get(start, end=None)")

    with open(__file__) as f:
        demo.text.insert('1.0', f.read())
    demo.text.update_stats()
    demo.pack(fill='both', expand=True)
    root.mainloop()