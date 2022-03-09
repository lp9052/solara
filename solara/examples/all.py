from solara.kitchensink import *
from .calculator import Calculator
from .bqplot import Plot
from .doc import Doc
from pathlib import Path

directory = Path(__file__).parent

md = open(directory / "README.md").read()


@react.component
def All():
    tab, set_tab = use_state(0, "tab")
    value, set_value = use_state(42.0, "value")
    print(tab)

    def set_tab2(value):
        print("set tab", value)
        set_tab(value)

    # md, set_md = use_state("")
    with v.Tabs(v_model=tab, on_v_model=set_tab2) as main:
        with v.Tab(children=["What is Solara ☀️?"]):
            pass
        with v.Tab(children=["Demo: calculator"]):
            pass
        with v.Tab(children=["Demo: bqplot"]):
            pass
        with v.Tab(children=["Docs"]):
            pass
        with v.TabsItems(v_model=tab):
            if tab == 0:
                # Markdown(md)
                w.FloatSlider(value=value, on_value=set_value)
                # w.Text(value=f"Square of {value} = {value**2}!")

                Markdown(md)
                # w.Textarea(value=md, on_value=set_md)
            if tab == 1:
                Calculator()
            if tab == 2:
                Plot()
            if tab == 3:
                Doc()

    return main


app = All()
