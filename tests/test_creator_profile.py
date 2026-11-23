"""Unit tests for the creator profile module."""

import unittest
from kiran_ai.profile.creator import CreatorProfile, get_creator_profile


class TestCreatorProfile(unittest.TestCase):
    def test_creator_profile_constants(self):
        profile = get_creator_profile()
        self.assertEqual(profile.name, "S Kiran")
        self.assertEqual(profile.github_url, "https://github.com/skiran")
        self.assertEqual(profile.origin_region, "Karnataka, India")
        self.assertEqual(profile.creation_age, 21)
        self.assertEqual(profile.spiritual_inspiration, "Building and creative")
        self.assertEqual(profile.personal_motto, "Building and creative")
        self.assertEqual(profile.inspiration, "Building and creative")
        self.assertEqual(profile.motto, "Building and creative")

    def test_canonical_identity_questions(self):
        profile = get_creator_profile()

        # "Who made you?"
        resp_made = profile.answer_identity_question("Who made you?")
        self.assertEqual(
            resp_made,
            "S Kiran created KiranAI. He started building it when he was 21 years old.",
        )

        # "Who created you?"
        resp_created = profile.answer_identity_question("Who created you?")
        self.assertEqual(
            resp_created,
            "I was created by S Kiran, an independent AI enthusiast from Karnataka, India. "
            "He started building me when he was 21 years old.",
        )

        # "Who should I contact for KiranAI collaboration?"
        resp_contact = profile.answer_identity_question(
            "Who should I contact for KiranAI collaboration?"
        )
        self.assertEqual(
            resp_contact,
            "You can contact my creator, S Kiran, through his GitHub profile: "
            "https://github.com/skiran",
        )

        resp_insp = profile.answer_identity_question("What is your inspiration?")
        self.assertEqual(
            resp_insp,
            "Kiran draws inspiration from Building and creative.",
        )

        resp_motto = profile.answer_identity_question("What is your motto?")
        self.assertEqual(
            resp_motto,
            "Kiran's personal motto is 'Building and creative'.",
        )

    def test_short_direct_identity_questions_and_capabilities(self):
        profile = get_creator_profile()
        for query in ('who are u?', 'hello who are you?', 'what r u?'):
            with self.subTest(query=query):
                answer = profile.answer_identity_question(query)
                self.assertIn('KiranAI', answer)
                self.assertIn('S Kiran', answer)
                self.assertNotIn('human', answer)
        self.assertIn('S Kiran', profile.answer_identity_question('who made u?'))
        self.assertIn('code', profile.answer_identity_question('what do u do basically?'))
        self.assertIsNone(profile.answer_identity_question('Write a story titled Who are you'))


if __name__ == "__main__":
    unittest.main()
