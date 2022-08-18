from icecream import ic
from modules import terminal_size, test_column_size
from modules import ScrollManager

if __name__ == "__main__":
    ic(terminal_size())
    test_column_size()
    t = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam iaculis venenatis finibus. Phasellus cursus erat et lectus porttitor, ac eleifend mauris interdum. Cras a ornare tortor. Proin placerat ultricies aliquet. Curabitur hendrerit ipsum et leo hendrerit faucibus. Morbi vehicula hendrerit ex a pretium. Integer ac est egestas, consequat eros rutrum, placerat ipsum. Maecenas consectetur tristique quam at sagittis. Maecenas ut imperdiet erat, nec lobortis diam.

Nullam ut ultrices nisi. Nulla facilisi. Mauris a justo non nisl luctus posuere. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum id nunc egestas, elementum augue id, porta enim. Aliquam ac augue quis odio rhoncus lobortis. In felis nisl, molestie tincidunt viverra a, pellentesque sed est.

Morbi nec lacus id tortor placerat efficitur sed in orci. Suspendisse interdum iaculis porta. Nulla purus nunc, gravida vel mauris quis, ullamcorper imperdiet est. Curabitur molestie vehicula augue, aliquam egestas tortor feugiat et. Nulla at sollicitudin odio. Donec consectetur commodo pellentesque. Nullam id orci non massa maximus pretium. Proin sed facilisis ex. Phasellus quis fermentum tellus, ac semper est. Suspendisse suscipit urna nec mollis aliquet. Donec sed commodo tellus.

Quisque orci neque, tempus vitae quam non, blandit convallis turpis. Phasellus laoreet euismod sem vitae convallis. Sed scelerisque augue ut massa ultrices, non porta sem finibus. Quisque aliquam quis arcu et faucibus. Proin augue libero, laoreet quis massa eget, aliquet blandit velit. Nunc imperdiet, est vel consectetur elementum, ante est molestie lorem, vitae malesuada velit sapien at nunc. Morbi facilisis leo massa. Etiam vulputate nunc mauris, feugiat maximus ipsum bibendum eget. Duis pharetra sit amet nunc eget tempus. Aliquam tempor metus felis, nec placerat magna tempor vitae. In in arcu vulputate, faucibus orci vitae, dictum sapien. Duis in nisi sed nisl sollicitudin consequat in et lectus. Phasellus ut justo risus. Mauris sit amet sodales est. Donec at dui iaculis, varius enim id, semper sem.

Nulla facilisi. Sed commodo, magna faucibus tincidunt viverra, lorem mauris commodo quam, ac vulputate felis neque ac nisi. Vestibulum viverra, eros eu tempus bibendum, eros odio ultrices turpis, a placerat mauris augue vitae sapien. Aliquam finibus vestibulum massa, nec sollicitudin mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Pellentesque faucibus tempus dui eget volutpat. Duis placerat dolor in leo congue vehicula. Morbi ornare pellentesque ligula, vel euismod enim varius venenatis. Nulla facilisi. Nam malesuada lacus id scelerisque luctus. Praesent fermentum sapien sit amet felis fringilla, ut mollis nibh malesuada. Sed faucibus metus eu diam accumsan, non malesuada erat efficitur. Vestibulum luctus urna eget mi vehicula, sit amet rutrum dui ornare. Donec maximus augue magna, eu dignissim justo vestibulum eu.""".split(".")
    scrolling_text = ScrollManager(data=t, viewable_lines=5)
    for _, _ in enumerate(t):
        if not scrolling_text.is_scrollable():
            break
        ic(scrolling_text.get_viewable_lines())
        scrolling_text.scroll()
