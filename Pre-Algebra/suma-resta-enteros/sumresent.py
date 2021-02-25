from manim import *
from manim.mobject.geometry import ArrowTriangleFilledTip

def update_Tex(str_arr):
    return Tex(
                str_arr[0],
                str_arr[1], 
                str_arr[2],
                str_arr[3], 
                color=TEAL_D
                ).shift(UP).scale(1.5)


class restaComoSuma(Scene):
    def construct(self):
        nl = NumberLine(
                x_min=-5.75,
                x_max=6,
                leftmost_tick=-5,
                include_numbers=True,
                include_ticks=False,
                include_tip=True
                )

        left_tip = Arrow(
                    start=[0, 0, 0],
                    end=[-6.25, 0, 0], 
                    color=LIGHT_GRAY,
                    stroke_width=0)

        dsp_arr = [
                    ["", "0", "", ""],
                    ["+ ", "1", "", ""],
                    ["+ ", "2", "", ""],
                    ["+ ", "3", "", ""],
                    ["+ ", "3", " - ", "1"],
                    ["+ ", "3", " - ", "2"],
                    ["+ ", "3", " - ", "3"],
                    ["", "0", "", ""],
                    ["- ", "1", "", ""],
                    ["- ", "2", "", ""],
                    ["- ", "3", "", ""],
                    ["- ", "3", " + ", "1"],
                    ["- ", "3", " + ", "2"],
                    ["- ", "3", " + ", "3"],
                    ["", "0", "", ""],
                  ]

        dot = Dot(color=TEAL_D, radius=0.15)
        curr_total = Tex("")
        last_total = Tex("")
        self.add(nl, left_tip, dot, curr_total, last_total)

        curr_total = update_Tex(dsp_arr[0])

        for i in range(len(dsp_arr) - 1):
            last_total =  curr_total
            curr_total = update_Tex(dsp_arr[i + 1])

            if i >= 3 and i < 10:
                if i != 6:
                    self.play(dot.animate.shift(LEFT), 
                          ReplacementTransform(last_total, curr_total))
                else:
                    self.play(ReplacementTransform(last_total, curr_total))
            else:
                if i != len(dsp_arr) - 2:
                    self.play(dot.animate.shift(RIGHT), 
                          ReplacementTransform(last_total, curr_total))
                else:
                    self.play(ReplacementTransform(last_total, curr_total))
            

        self.wait()


class conmutacion(Scene):
    def construct(self):
        pass        
