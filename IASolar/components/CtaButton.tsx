type Props = {
  onClick?: () => void;
  children: React.ReactNode;
};

export default function CtaButton({ onClick, children }: Props) {
  return (
    <button className="cta" onClick={onClick}>
      {children}
    </button>
  );
}
