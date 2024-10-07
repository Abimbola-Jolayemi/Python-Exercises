import unittest
import tv


class MyTestCase(unittest.TestCase):
    def test_that_television_exists(self):
        television = tv.Tv()

    def test_that_television_is_off_by_default(self):
        television = tv.Tv()
        self.assertFalse(television.get_tv_state())

    def test_that_television_can_be_turned_on(self):
        television = tv.Tv()
        self.assertFalse(television.get_tv_state())
        television.turn_on()
        self.assertTrue(television.get_tv_state())

    def test_that_television_can_be_turned_off_after_turning_on(self):
        television = tv.Tv()
        self.assertFalse(television.get_tv_state())
        television.turn_on()
        self.assertTrue(television.get_tv_state())
        television.turn_off()
        self.assertFalse(television.get_tv_state())

    def test_that_television_channel_can_only_be_changed_when_television_is_on(self):
        television = tv.Tv()
        television.turn_on()
        television.channel_up()
        self.assertEqual(television.get_channel(), 1)

    def test_that_television_default_channel_is_0(self):
        television = tv.Tv()
        television.turn_on()
        self.assertEqual(television.get_channel(), 0)

    def test_that_television_channel_can_be_set(self):
        television = tv.Tv()
        television.turn_on()
        self.assertEqual(television.get_channel(), 0)
        television.set_channel(5)
        self.assertEqual(television.get_channel(), 5)

    def test_that_television_channel_cannot_be_set_to_a_negative_number(self):
        television = tv.Tv()
        television.turn_on()
        self.assertEqual(television.get_channel(), 0)
        television.set_channel(-5)
        self.assertEqual(television.get_channel(), 0)

    def test_that_television_channel_cannot_be_set_to_above_100(self):
        television = tv.Tv()
        television.turn_on()
        self.assertEqual(television.get_channel(), 0)
        television.set_channel(105)
        self.assertEqual(television.get_channel(), 0)

    def test_that_television_channel_can_be_increased(self):
        television = tv.Tv()
        television.turn_on()
        self.assertEqual(television.get_channel(), 0)
        television.channel_up()
        self.assertEqual(television.get_channel(), 1)
        television.set_channel(5)
        television.channel_up()
        self.assertEqual(television.get_channel(), 6)

    def test_that_television_channel_cannot_be_increased_above_100(self):
        television = tv.Tv()
        television.turn_on()
        television.set_channel(100)
        television.channel_up()
        self.assertEqual(television.get_channel(), 100)

    def test_that_television_channel_can_be_decreased(self):
        television = tv.Tv()
        television.turn_on()
        television.set_channel(89)
        television.channel_down()
        self.assertEqual(television.get_channel(), 88)

    def test_that_television_channel_cannot_be_decreased_below_0(self):
        television = tv.Tv()
        television.turn_on()
        television.set_channel(0)
        television.channel_down()
        self.assertEqual(television.get_channel(), 0)

    def test_that_television_default_volume_is_0_when_tv_is_on(self):
        television = tv.Tv()
        television.turn_on()
        self.assertEqual(television.get_volume(), 0)

    def test_that_tv_is_on_and_volume_can_be_set(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(6)
        self.assertEqual(television.get_volume(), 6)

    def test_that_television_is_on_and_volume_cannot_be_set_to_a_value_below_zero(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(-1)
        self.assertEqual(television.get_volume(), 0)

    def test_that_television_is_on_and_volume_cannot_be_set_to_a_value_above_10(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(11)
        self.assertEqual(television.get_volume(), 0)

    def test_that_television_is_on_and_volume_can_be_increased(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(6)
        self.assertEqual(television.get_volume(), 6)
        television.volume_up()
        self.assertEqual(television.get_volume(), 7)

    def test_that_television_is_on_and_volume_cannot_be_increased_above_10(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(10)
        self.assertEqual(television.get_volume(), 10)
        television.volume_up()
        self.assertEqual(television.get_volume(), 10)

    def test_that_tv_is_on_and_can_be_decreased(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(10)
        television.volume_down()
        self.assertEqual(television.get_volume(), 9)

    def test_that_tv_is_on_and_cannot_be_decreased_below_0(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(0)
        television.volume_down()
        self.assertEqual(television.get_volume(), 0)

    def test_that_television_can_return_to_its_previous_channel_after_turning_on(self):
        television = tv.Tv()
        television.turn_on()
        television.set_channel(12)
        self.assertEqual(television.get_channel(), 12)
        television.turn_off()
        television.turn_on()
        self.assertEqual(television.get_channel(), 12)

    def test_that_television_volume_returns_to_zero_after_turning_off(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(7)
        self.assertEqual(television.get_volume(), 7)
        television.turn_off()
        self.assertEqual(television.get_volume(), 0)

    def test_that_television_volume_can_be_muted_and_volume_becomes_zero(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(7)
        self.assertEqual(television.get_volume(), 7)
        television.mute()
        self.assertEqual(television.get_volume(), 0)

    def test_that_television_volume_can_be_un_muted_and_volume_returns_to_previous_volume(self):
        television = tv.Tv()
        television.turn_on()
        television.set_volume(7)
        television.mute()
        television.unmute()
        self.assertEqual(television.get_volume(), 7)



if __name__ == '__main__':
    unittest.main()
