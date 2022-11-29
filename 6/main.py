from message import Message
from savecommand import SaveCommand
from discardcommand import DiscardCommand
from printcommand import PrintCommand
from rule import Rule
from senderrule import SenderRule
from anyrule import AnyRule

rule: Rule
# ここでルールを組み立てる．
rule1 = SenderRule(SaveCommand(), "alice")
rule2 = SenderRule(DiscardCommand(), "bob")
rule3 = AnyRule(PrintCommand())
rule1.set_next(rule2).set_next(rule3)

msgs = [
    Message("alice", "me", "Hello, this is Alice."),
    Message("bob", "me", "Hello from Bob."),
    Message("charlie", "me", "Hi, it's Charlie.")
]

for m in msgs:
    # ここでメッセージmについてルールを実行する．
    rule1.handle(m)
