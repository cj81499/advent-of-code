import unittest
import day20

regex1 = "^WNE$"
regex2 = "^ENWWW(NEEE|SSE(EE|N))$"
regex3 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
regex4 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
regex5 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"


class TestDay20(unittest.TestCase):
    def test_day20_facility_1(self):
        fac = day20.Facility(regex1)
        self.assertEqual("""#####
#.|.#
#-###
#.|X#
#####""", str(fac))

    def test_day20_facility_2(self):
        fac = day20.Facility(regex2)
        self.assertEqual("""#########
#.|.|.|.#
#-#######
#.|.|.|.#
#-#####-#
#.#.#X|.#
#-#-#####
#.|.|.|.#
#########""", str(fac))

    def test_day20_facility_3(self):
        fac = day20.Facility(regex3)
        self.assertEqual("""###########
#.|.#.|.#.#
#-###-#-#-#
#.|.|.#.#.#
#-#####-#-#
#.#.#X|.#.#
#-#-#####-#
#.#.|.|.|.#
#-###-###-#
#.|.|.#.|.#
###########""", str(fac))

    def test_day20_facility_4(self):
        fac = day20.Facility(regex4)
        self.assertEqual("""#############
#.|.|.|.|.|.#
#-#####-###-#
#.#.|.#.#.#.#
#-#-###-#-#-#
#.#.#.|.#.|.#
#-#-#-#####-#
#.#.#.#X|.#.#
#-#-#-###-#-#
#.|.#.|.#.#.#
###-#-###-#-#
#.|.#.|.|.#.#
#############""", str(fac))

    def test_day20_facility_5(self):
        fac = day20.Facility(regex5)
        self.assertEqual("""###############
#.|.|.|.#.|.|.#
#-###-###-#-#-#
#.|.#.|.|.#.#.#
#-#########-#-#
#.#.|.|.|.|.#.#
#-#-#########-#
#.#.#.|X#.|.#.#
###-#-###-#-#-#
#.|.#.#.|.#.|.#
#-###-#####-###
#.|.#.|.|.#.#.#
#-#-#####-#-#-#
#.#.|.|.|.#.|.#
###############""", str(fac))

    def test_day20_parta_1(self):
        fac = day20.Facility(regex1)
        self.assertEqual(3, fac.furthest_room_dist())

    def test_day20_parta_2(self):
        fac = day20.Facility(regex2)
        self.assertEqual(10, fac.furthest_room_dist())

    def test_day20_parta_3(self):
        fac = day20.Facility(regex3)
        self.assertEqual(18, fac.furthest_room_dist())

    def test_day20_parta_4(self):
        fac = day20.Facility(regex4)
        self.assertEqual(23, fac.furthest_room_dist())

    def test_day20_parta_5(self):
        fac = day20.Facility(regex5)
        self.assertEqual(31, fac.furthest_room_dist())

    # def test_day20_partb(self):
    #     self.assertEqual(0, day20.partb(lines))


if __name__ == "__main__":
    unittest.main()
