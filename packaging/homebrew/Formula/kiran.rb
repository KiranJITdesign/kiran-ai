class Kiran < Formula
  desc "KiranAI: Original, open-weight AI system under 50 MB"
  homepage "https://github.com/skiran"
  url "https://github.com/skiran/KiranAI/archive/refs/tags/v0.1.0.tar.gz"
  license "Apache-2.0"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/kiran", "version"
  end
end

