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
        nl = NumberLine(x_min=-5.75,
                        x_max=6,
                        leftmost_tick=-5,
                        include_numbers=True,
                        include_ticks=False,
                        include_tip=True)

        left_tip = Arrow(start=[0, 0, 0],
                         end=[-6.25, 0, 0], 
                         color=LIGHT_GRAY,
                         stroke_width=0)

        dsp_arr = [["", "0", "", ""],
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
                   ["", "0", "", ""]]

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
        nl = NumberLine(x_min=-5.75,
                        x_max=6,
                        leftmost_tick=-5,
                        include_numbers=True,
                        include_ticks=False,
                        include_tip=True)

        left_tip = Arrow(start=[0, 0, 0],
                         end=[-6.25, 0, 0], 
                         color=LIGHT_GRAY,
                         stroke_width=0)

        text_array1 = ["0", "2", "2 + 3", "2 + 3 = 5"]
        text_array2 = ["0", "3", "3 + 2", "3 + 2 = 5"]

        first_tex = Tex("")
        second_tex = Tex("")
        last_tex = Tex("")

        dot = Dot(color=TEAL_D, radius=0.15)

        first_tex = Tex(text_array1[0], color=TEAL_D).shift(UP + 2.5 * RIGHT).scale(1.5)
        second_tex = Tex(text_array2[0], color=TEAL_D).shift(UP + 2.5 * RIGHT).scale(1.5)

        self.add(nl, left_tip, first_tex, dot)
        self.wait()

        for i in range(len(text_array1)):
            last_tex = first_tex
            first_tex = Tex(text_array1[i], color=TEAL_D
                       ).shift(UP + 2.5 * RIGHT).scale(1.5)

            if i < 3:
                self.play(dot.animate.shift(int(text_array1[i][-1]) * RIGHT),
                          ReplacementTransform(last_tex, first_tex))
            else:
                self.play(ReplacementTransform(last_tex, first_tex))

        self.play(first_tex.animate.shift(5 * LEFT))
        self.play(dot.animate.shift(5 * LEFT), FadeIn(second_tex))

        for i in range(len(text_array2)):
            last_tex = second_tex
            second_tex = Tex(text_array2[i], color=TEAL_D
                       ).shift(UP + 2.5 * RIGHT).scale(1.5)

            if i < 3:
                self.play(dot.animate.shift(int(text_array2[i][-1]) * RIGHT),
                          ReplacementTransform(last_tex, second_tex))
            else:
                self.play(ReplacementTransform(last_tex, second_tex))

        last_tex = Tex("2 + 3 = 3 + 2", color=TEAL_D
                       ).shift(UP).scale(1.5)

        self.play(ReplacementTransform(first_tex, last_tex),
                  ReplacementTransform(second_tex, last_tex))

        self.wait()
