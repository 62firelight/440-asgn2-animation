from manim import *


class PageAllocation(Scene):
    def construct(self):
        # Head and tail arrows
        head_arrow = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).rotate(-90*DEGREES).scale(0.4).move_to(page.get_corner(UL) + 0.45 * LEFT)
        head_text = Tex("Head").next_to(head_arrow, direction=LEFT)
        head = Group(head_arrow, head_text)
        
        tail_arrow = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).rotate(90*DEGREES).scale(0.4).move_to(page.get_corner(UR) + 0.45 * RIGHT)
        tail_text = Tex("Tail").next_to(tail_arrow, direction=RIGHT)
        tail = Group(tail_arrow, tail_text)
        
        arrow_group = Group(head, tail)
        
        # Terminal commands
        write_half_page_text = Text("sudo ./data_generator 2048bytes.txt", font='Monospace').to_edge(UP).shift(0.45 * UP).scale(0.75)
        write_full_page_text = Text("sudo ./data_generator 6144bytes.txt", font='Monospace').to_edge(UP).shift(0.45 * UP).scale(0.75)
        read_data_text = Text("cat /dev/asgn2", font='Monospace').to_edge(UP).shift(0.45 * UP).scale(0.75)
        
        # First page
        page = Rectangle(width=3, height=6)
        first_page_text = Text("Page 1")
        first_page_text.move_to(page.get_edge_center(DOWN) + 0.5 * DOWN)
        
        # Fill the first half of a page with unread data
        empty_filled_page = Rectangle(width=3, height=0).move_to(page.get_edge_center(UP))
        
        half_filled_page = Rectangle(width=3, height=3, fill_color=ORANGE, fill_opacity=1)
        half_filled_page.move_to(page.get_edge_center(UP) + (half_filled_page.height / 2) * DOWN)

        # Read the first half of a page
        empty_read_page = Rectangle(width=3, height=0).move_to(page.get_edge_center(UP))
        half_read_page = half_filled_page.copy()
        half_read_page.set_fill_color(RED)
        
        # Fill the second half of a page with unread data
        full_filled_page1 = Rectangle(width=3, height=0, fill_color=ORANGE, fill_opacity=1)
        
        full_filled_page2 = Rectangle(width=3, height=3, fill_color=ORANGE, fill_opacity=1)
        full_filled_page2.move_to((full_filled_page2.height / 2) * DOWN)

        # Read the second half of a page
        full_read_page1 = Rectangle(width=3, height=0, fill_color=RED, fill_opacity=1)
        
        full_read_page2 = Rectangle(width=3, height=3, fill_color=RED, fill_opacity=1)
        full_read_page2.shift((full_read_page2.height / 2) * DOWN + 3 * LEFT)
        
        # Group first page objects together
        first_page_group = Group(page, empty_filled_page, empty_read_page, full_filled_page1, full_read_page1, first_page_text)
        
        # Second page
        second_page = page.copy().shift(3 * RIGHT)
        second_page_text = Text("Page 2")
        second_page_text.move_to(second_page.get_edge_center(DOWN) + 0.5 * DOWN)
        
        # Fill the entire second page with unread data
        empty_filled_second_page = Rectangle(width=3, height=0, fill_color=ORANGE, fill_opacity=1)
        empty_filled_second_page.move_to(second_page.get_edge_center(UP))
        
        full_filled_second_page = Rectangle(width=3, height=6, fill_color=ORANGE, fill_opacity=1)
        full_filled_second_page.move_to(second_page.get_center())
        
        # Read the entire second page
        empty_read_second_page = Rectangle(width=3, height=0, fill_color=RED, fill_opacity=1)

        full_read_second_page = Rectangle(width=3, height=6, fill_color=RED, fill_opacity=1)
        
        # Group second page mobjects together
        second_page_group = Group(second_page, empty_filled_second_page, second_page_text)
        
        # self.add(page, head, tail, empty_filled_page, empty_read_page, first_page_text)
        
        # Animations
        self.play(Create(empty_filled_page), FadeIn(head), FadeIn(tail), Create(empty_read_page))
        
        self.play(Write(write_half_page_text))
        
        self.play(Create(page))
        
        self.play(Write(first_page_text))
        
        self.play(tail.animate.shift(3 * DOWN), Transform(empty_filled_page, half_filled_page, about_edge=UP))
        
        self.play(Transform(write_half_page_text, read_data_text))
        
        self.play(head.animate.shift(3 * DOWN), Transform(empty_read_page, half_read_page, about_edge=UP))
        
        self.play(Transform(write_half_page_text, write_full_page_text))
        
        self.play(tail.animate.shift(3 * DOWN), Transform(full_filled_page1, full_filled_page2, about_edge=UP))
        
        self.play(first_page_group.animate.shift(3 * LEFT), arrow_group.animate.shift(3 * LEFT))
        
        self.play(Create(second_page), Write(second_page_text))
        
        self.play(tail.animate.move_to(second_page.get_corner(UR) + 1.05 * RIGHT))
        
        self.play(tail.animate.shift(6 * DOWN), Transform(empty_filled_second_page, full_filled_second_page))
        
        self.add(full_read_page1)
        self.remove(half_filled_page)
        self.remove(half_read_page)
        
        self.play(Transform(write_half_page_text, read_data_text))
        
        self.play(head.animate.shift(3 * DOWN), Transform(full_read_page1, full_read_page2, about_edge=UP)) 
        
        self.play(FadeOut(first_page_group))
        
        self.play(head.animate.move_to(second_page.get_corner(UL) + 1.1 * LEFT))
        
        self.play(arrow_group.animate.shift(3 * LEFT), second_page_group.animate.shift(3 * LEFT), FadeOut(second_page_text))
        
        first_page_text.move_to(second_page.get_edge_center(DOWN) + 0.5 * DOWN)
        
        self.play(Write(first_page_text))
        
        self.add(empty_read_second_page)
        empty_read_second_page.move_to(second_page.get_edge_center(UP))
        
        self.play(head.animate.shift(6 * DOWN), Transform(empty_read_second_page, full_read_second_page))
        
        self.wait(3)