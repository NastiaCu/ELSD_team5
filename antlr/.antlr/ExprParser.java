// Generated from c:\Users\micha\OneDrive\Desktop\University\Semestrul IV\PBL\ELSD_team5\antlr\Expr.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, STRING=20, NEWLINE=21, INT=22, CHR=23, WS=24;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_query_invocation = 2, RULE_term = 3, 
		RULE_variable = 4, RULE_variable_declaration = 5, RULE_method_invocation = 6, 
		RULE_method_name = 7, RULE_assignment_statement = 8, RULE_method_declaration = 9, 
		RULE_comments = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "query_invocation", "term", "variable", "variable_declaration", 
			"method_invocation", "method_name", "assignment_statement", "method_declaration", 
			"comments"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'func process()'", "'{'", "'}'", "'func compose()'", "'='", "'('", 
			"','", "')'", "'load'", "'delay'", "'setreverb'", "'setgain'", "'changepitch'", 
			"'fadein'", "'fadeout'", "'play'", "'splice'", "'func '", "'//'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "STRING", "NEWLINE", 
			"INT", "CHR", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<TerminalNode> NEWLINE() { return getTokens(ExprParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ExprParser.NEWLINE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(T__0);
			setState(23);
			match(T__1);
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << NEWLINE) | (1L << CHR))) != 0)) {
				{
				{
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NEWLINE) {
					{
					setState(24);
					match(NEWLINE);
					}
				}

				setState(27);
				statement();
				setState(29);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
				case 1:
					{
					setState(28);
					match(NEWLINE);
					}
					break;
				}
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(36);
			match(T__2);
			setState(37);
			match(NEWLINE);
			setState(38);
			match(T__3);
			setState(39);
			match(T__1);
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << NEWLINE) | (1L << CHR))) != 0)) {
				{
				{
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NEWLINE) {
					{
					setState(40);
					match(NEWLINE);
					}
				}

				setState(43);
				statement();
				setState(45);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(44);
					match(NEWLINE);
					}
					break;
				}
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public Query_invocationContext query_invocation() {
			return getRuleContext(Query_invocationContext.class,0);
		}
		public CommentsContext comments() {
			return getRuleContext(CommentsContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(56);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case CHR:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				query_invocation();
				}
				break;
			case T__18:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				comments();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Query_invocationContext extends ParserRuleContext {
		public Variable_declarationContext variable_declaration() {
			return getRuleContext(Variable_declarationContext.class,0);
		}
		public Method_invocationContext method_invocation() {
			return getRuleContext(Method_invocationContext.class,0);
		}
		public Method_declarationContext method_declaration() {
			return getRuleContext(Method_declarationContext.class,0);
		}
		public Assignment_statementContext assignment_statement() {
			return getRuleContext(Assignment_statementContext.class,0);
		}
		public Query_invocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query_invocation; }
	}

	public final Query_invocationContext query_invocation() throws RecognitionException {
		Query_invocationContext _localctx = new Query_invocationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_query_invocation);
		try {
			setState(62);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(58);
				variable_declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				method_invocation();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(60);
				method_declaration();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(61);
				assignment_statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_term);
		try {
			setState(66);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CHR:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				variable();
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(65);
				match(INT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode CHR() { return getToken(ExprParser.CHR, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(CHR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_declarationContext extends ParserRuleContext {
		public List<TerminalNode> CHR() { return getTokens(ExprParser.CHR); }
		public TerminalNode CHR(int i) {
			return getToken(ExprParser.CHR, i);
		}
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public Method_invocationContext method_invocation() {
			return getRuleContext(Method_invocationContext.class,0);
		}
		public Variable_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_declaration; }
	}

	public final Variable_declarationContext variable_declaration() throws RecognitionException {
		Variable_declarationContext _localctx = new Variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_variable_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(CHR);
			setState(71);
			match(T__4);
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(72);
				match(INT);
				}
				break;
			case CHR:
				{
				setState(73);
				match(CHR);
				}
				break;
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
				{
				setState(74);
				method_invocation();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_invocationContext extends ParserRuleContext {
		public Method_nameContext method_name() {
			return getRuleContext(Method_nameContext.class,0);
		}
		public List<TerminalNode> INT() { return getTokens(ExprParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(ExprParser.INT, i);
		}
		public List<TerminalNode> CHR() { return getTokens(ExprParser.CHR); }
		public TerminalNode CHR(int i) {
			return getToken(ExprParser.CHR, i);
		}
		public List<TerminalNode> STRING() { return getTokens(ExprParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExprParser.STRING, i);
		}
		public Method_invocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_invocation; }
	}

	public final Method_invocationContext method_invocation() throws RecognitionException {
		Method_invocationContext _localctx = new Method_invocationContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_method_invocation);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			method_name();
			setState(78);
			match(T__5);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STRING) | (1L << INT) | (1L << CHR))) != 0)) {
				{
				{
				setState(79);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STRING) | (1L << INT) | (1L << CHR))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(88);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(85);
					match(T__6);
					}
					} 
				}
				setState(90);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			setState(91);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_nameContext extends ParserRuleContext {
		public Method_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_name; }
	}

	public final Method_nameContext method_name() throws RecognitionException {
		Method_nameContext _localctx = new Method_nameContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_method_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assignment_statementContext extends ParserRuleContext {
		public List<TerminalNode> CHR() { return getTokens(ExprParser.CHR); }
		public TerminalNode CHR(int i) {
			return getToken(ExprParser.CHR, i);
		}
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public Assignment_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment_statement; }
	}

	public final Assignment_statementContext assignment_statement() throws RecognitionException {
		Assignment_statementContext _localctx = new Assignment_statementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_assignment_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(CHR);
			setState(96);
			match(T__4);
			setState(97);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==CHR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declarationContext extends ParserRuleContext {
		public List<TerminalNode> CHR() { return getTokens(ExprParser.CHR); }
		public TerminalNode CHR(int i) {
			return getToken(ExprParser.CHR, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ExprParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ExprParser.NEWLINE, i);
		}
		public Method_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declaration; }
	}

	public final Method_declarationContext method_declaration() throws RecognitionException {
		Method_declarationContext _localctx = new Method_declarationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_method_declaration);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(T__17);
			setState(100);
			match(CHR);
			setState(101);
			match(T__5);
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CHR) {
				{
				{
				setState(102);
				match(CHR);
				}
				}
				setState(107);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(111);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(108);
					match(T__6);
					}
					} 
				}
				setState(113);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			setState(114);
			match(T__7);
			setState(115);
			match(T__1);
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << NEWLINE) | (1L << CHR))) != 0)) {
				{
				{
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NEWLINE) {
					{
					setState(116);
					match(NEWLINE);
					}
				}

				setState(119);
				statement();
				setState(121);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
				case 1:
					{
					setState(120);
					match(NEWLINE);
					}
					break;
				}
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(128);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CommentsContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(ExprParser.STRING, 0); }
		public CommentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comments; }
	}

	public final CommentsContext comments() throws RecognitionException {
		CommentsContext _localctx = new CommentsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_comments);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			match(T__18);
			setState(131);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32\u0088\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\3\2\3\2\3\2\5\2\34\n\2\3\2\3\2\5\2 \n\2\7\2\"\n\2\f\2\16"+
		"\2%\13\2\3\2\3\2\3\2\3\2\3\2\5\2,\n\2\3\2\3\2\5\2\60\n\2\7\2\62\n\2\f"+
		"\2\16\2\65\13\2\3\2\3\2\3\3\3\3\5\3;\n\3\3\4\3\4\3\4\3\4\5\4A\n\4\3\5"+
		"\3\5\5\5E\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7N\n\7\3\b\3\b\3\b\7\bS\n"+
		"\b\f\b\16\bV\13\b\3\b\7\bY\n\b\f\b\16\b\\\13\b\3\b\3\b\3\t\3\t\3\n\3\n"+
		"\3\n\3\n\3\13\3\13\3\13\3\13\7\13j\n\13\f\13\16\13m\13\13\3\13\7\13p\n"+
		"\13\f\13\16\13s\13\13\3\13\3\13\3\13\5\13x\n\13\3\13\3\13\5\13|\n\13\7"+
		"\13~\n\13\f\13\16\13\u0081\13\13\3\13\3\13\3\f\3\f\3\f\3\f\4Zq\2\r\2\4"+
		"\6\b\n\f\16\20\22\24\26\2\5\4\2\26\26\30\31\3\2\13\23\3\2\30\31\2\u0090"+
		"\2\30\3\2\2\2\4:\3\2\2\2\6@\3\2\2\2\bD\3\2\2\2\nF\3\2\2\2\fH\3\2\2\2\16"+
		"O\3\2\2\2\20_\3\2\2\2\22a\3\2\2\2\24e\3\2\2\2\26\u0084\3\2\2\2\30\31\7"+
		"\3\2\2\31#\7\4\2\2\32\34\7\27\2\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35\3"+
		"\2\2\2\35\37\5\4\3\2\36 \7\27\2\2\37\36\3\2\2\2\37 \3\2\2\2 \"\3\2\2\2"+
		"!\33\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%#\3\2\2\2&\'\7\5"+
		"\2\2\'(\7\27\2\2()\7\6\2\2)\63\7\4\2\2*,\7\27\2\2+*\3\2\2\2+,\3\2\2\2"+
		",-\3\2\2\2-/\5\4\3\2.\60\7\27\2\2/.\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2"+
		"\61+\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65"+
		"\63\3\2\2\2\66\67\7\5\2\2\67\3\3\2\2\28;\5\6\4\29;\5\26\f\2:8\3\2\2\2"+
		":9\3\2\2\2;\5\3\2\2\2<A\5\f\7\2=A\5\16\b\2>A\5\24\13\2?A\5\22\n\2@<\3"+
		"\2\2\2@=\3\2\2\2@>\3\2\2\2@?\3\2\2\2A\7\3\2\2\2BE\5\n\6\2CE\7\30\2\2D"+
		"B\3\2\2\2DC\3\2\2\2E\t\3\2\2\2FG\7\31\2\2G\13\3\2\2\2HI\7\31\2\2IM\7\7"+
		"\2\2JN\7\30\2\2KN\7\31\2\2LN\5\16\b\2MJ\3\2\2\2MK\3\2\2\2ML\3\2\2\2N\r"+
		"\3\2\2\2OP\5\20\t\2PT\7\b\2\2QS\t\2\2\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2"+
		"TU\3\2\2\2UZ\3\2\2\2VT\3\2\2\2WY\7\t\2\2XW\3\2\2\2Y\\\3\2\2\2Z[\3\2\2"+
		"\2ZX\3\2\2\2[]\3\2\2\2\\Z\3\2\2\2]^\7\n\2\2^\17\3\2\2\2_`\t\3\2\2`\21"+
		"\3\2\2\2ab\7\31\2\2bc\7\7\2\2cd\t\4\2\2d\23\3\2\2\2ef\7\24\2\2fg\7\31"+
		"\2\2gk\7\b\2\2hj\7\31\2\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2lq\3"+
		"\2\2\2mk\3\2\2\2np\7\t\2\2on\3\2\2\2ps\3\2\2\2qr\3\2\2\2qo\3\2\2\2rt\3"+
		"\2\2\2sq\3\2\2\2tu\7\n\2\2u\177\7\4\2\2vx\7\27\2\2wv\3\2\2\2wx\3\2\2\2"+
		"xy\3\2\2\2y{\5\4\3\2z|\7\27\2\2{z\3\2\2\2{|\3\2\2\2|~\3\2\2\2}w\3\2\2"+
		"\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081"+
		"\177\3\2\2\2\u0082\u0083\7\5\2\2\u0083\25\3\2\2\2\u0084\u0085\7\25\2\2"+
		"\u0085\u0086\7\26\2\2\u0086\27\3\2\2\2\23\33\37#+/\63:@DMTZkqw{\177";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}