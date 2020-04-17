from gitlint.rules import CommitRule, RuleViolation, LineRule, CommitMessageBody, CommitMessageTitle
from gitlint.options import IntOption, ListOption
from gitlint import utils


class SignedOffBy(CommitRule):
    """ This rule will enforce that each commit contains a "Signed-Off-By" line.
    We keep things simple here and just check whether the commit body contains a line that starts with "Signed-Off-By".
    """

    # A rule MUST have a human friendly name
    name = "body-requires-signed-off-by"

    # A rule MUST have a *unique* id, we recommend starting with UC (for User-defined Commit-rule).
    id = "UC1"

    def validate(self, commit):
        for line in commit.message.body:
            if line.startswith("Signed-off-by"):
                return

        return [RuleViolation(self.id, "Body does not contain a 'Signed-Off-By' line", line_nr=1)]

class MaxLineLengthCustom(LineRule):
    name = "max-line-length-custom"
    id = "UR1"
    target = CommitMessageBody
    options_spec = [IntOption('line-length', 80, "Max line length"),
                    IntOption('warn-line-length', 78, "Warning about line length")]
    warning_message = "{2} WARNING: Line exceeds max length ({0}>{1}): \"{3}\""
    violation_message = "Line exceeds max length ({0}>{1})"

    def validate(self, line, _commit):
        max_length = self.options['line-length'].value
        warn_length = self.options['warn-line-length'].value
        if len(line) > max_length:
            return [RuleViolation(self.id, self.violation_message.format(len(line), max_length), line)]
        elif len(line) > warn_length:
            print self.warning_message.format(len(line), warn_length,
                                              self.id, line)

class BodyMaxLineLengthCustom(MaxLineLengthCustom):
    name = "body-max-line-length-custom"
    id = "UB1"
    target = CommitMessageBody
    options_spec = [IntOption('line-length', 80, "Max line length"),
                IntOption('warn-line-length', 78, "Warning about line length")]

class TitleMaxLengthCustom(MaxLineLengthCustom):
    name = "title-max-length-custom"
    id = "UT1"
    target = CommitMessageTitle
    options_spec = [IntOption('line-length', 65, "Max line length"),
                IntOption('warn-line-length', 50, "Warning about line length")]
    violation_message = "Title exceeds max length ({0}>{1})"
    warning_message = "{2} WARNING: Title exceeds max length ({0}>{1}): \"{3}\""
